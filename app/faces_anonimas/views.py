# app/faces/views.py
import cv2
import tempfile
from django.core.files import File
from app.faces_anonimas.models import FaceAnonima

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