from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
import numpy as np
import cv2
from scripts.captura_facial import process_faces_with_face_recognition, extract_face_from_frame
from .models import Face, Usuario


class FaceRegisterView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        user_id = request.data.get("usuario_id")
        files = request.FILES.getlist("frames")

        if not user_id or not files:
            return Response({
                "success": False,
                "message": "ID do usuário e frames são obrigatórios."
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            usuario = Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return Response({
                "success": False,
                "message": "Usuário não encontrado."
            }, status=status.HTTP_404_NOT_FOUND)

        frames = []
        for file in files:
            file_bytes = np.frombuffer(file.read(), np.uint8)
            frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            if frame is not None:
                frames.append(frame)

        if not frames:
            return Response({
                "success": False,
                "message": "Nenhuma imagem válida foi enviada."
            }, status=status.HTTP_400_BAD_REQUEST)

        vector = process_faces_with_face_recognition(frames)
        if not vector:
            return Response({
                "success": False,
                "message": "Nenhum rosto detectado nos frames."
            }, status=status.HTTP_400_BAD_REQUEST)

        face = Face.objects.create(
            usuario=usuario,
            arr_imagem=vector
        )

        return Response({
            "success": True,
            "face_id": face.id,
            "usuario_id": usuario.id
        }, status=status.HTTP_201_CREATED)