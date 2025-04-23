# app/faces/views.py
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from app.faces_anonimas.models import FaceAnonima
from app.tentativas_acesso_anonimo.models import TentativaAcessoAnonimo
from app.faces_anonimas.serializers import FaceAnonimaSerializer
from rest_framework.generics import DestroyAPIView

class FaceAnonimaRegisterView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        tentativa_id = request.data.get("id_tentativa_acesso_anonimo")
        imagem = request.FILES.get("img_anonimo")

        if not tentativa_id or not imagem:
            return Response({
                "success": False,
                "message": "ID da tentativa e imagem são obrigatórios."
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            tentativa = TentativaAcessoAnonimo.objects.get(pk=tentativa_id)
        except TentativaAcessoAnonimo.DoesNotExist:
            return Response({
                "success": False,
                "message": "Tentativa de acesso não encontrada."
            }, status=status.HTTP_404_NOT_FOUND)

        face_anonima = FaceAnonima.objects.create(
            id_tentativa_acesso_anonimo=tentativa,
            img_anonimo=imagem
        )

        serializer = FaceAnonimaSerializer(face_anonima)
        return Response({
            "success": True,
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)


class FaceAnonimaDeleteView(DestroyAPIView):
    queryset = FaceAnonima.objects.all()
    serializer_class = FaceAnonimaSerializer
    lookup_field = 'id'