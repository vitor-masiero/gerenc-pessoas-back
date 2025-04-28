# app/faces/views.py
import cv2
import tempfile
from django.core.files import File
from app.faces_anonimas.models import FaceAnonima
from rest_framework import generics
from app.faces_anonimas.serializers import FaceAnonimaSerializer

def criar_face_anonima(tentativa_acesso_anonimo, frame, usuario=None):
    with tempfile.NamedTemporaryFile(suffix=".jpg") as temp_img:
        cv2.imwrite(temp_img.name, frame)
        temp_img.seek(0)
        nome_arquivo = f"anonima_{usuario.id}.jpg" if usuario else "anonima_desconhecida.jpg"
        face = FaceAnonima.objects.create(
            id_tentativa_acesso_anonimo=tentativa_acesso_anonimo,
            img_anonimo=File(temp_img, name=nome_arquivo)
        )
        return face

class FacesAnonimasPorEmpresaView(generics.ListAPIView):
    serializer_class = FaceAnonimaSerializer

    def get_queryset(self):
        empresa_id = self.request.query_params.get('empresa_id')
        if not empresa_id:
            return FaceAnonima.objects.none()

        try:
            empresa_id = int(empresa_id)
        except ValueError:
            return FaceAnonima.objects.none()

        return FaceAnonima.objects.filter(
            id_tentativa_acesso_anonimo__id_empresa__id=empresa_id
        ).order_by('-dt_criado')
    
class FacesAnonimas(generics.ListAPIView):
    queryset=FaceAnonima.objects.all()
    serializer_class = FaceAnonimaSerializer