from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
import numpy as np
import cv2
from app.scripts.captura_facial import process_faces_with_face_recognition, extract_face_from_frame
from app.faces.models import Face
from app.usuarios.models import Usuario
from app.empresas.models import Empresa
from app.tentativas_acesso.models import TentativaAcesso
from app.tentativas_acesso_anonimo.models import TentativaAcessoAnonimo
from app.usuarios_empresas.models import UsuarioEmpresa
from rest_framework.generics import DestroyAPIView
from app.faces.serializers import FaceSerializer
from scipy.spatial.distance import cosine
from app.alertas.services.alerta_service import registrar_alerta
from app.faces_anonimas.views import criar_face_anonima


#POST
class FaceRegisterView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        user_id = request.data.get("usuario_id")
        files = request.FILES.getlist("frames")

        if not user_id or not files:
            print("ID do usuário e frames são obrigatórios.")
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
            print("Nenhuma imagem válida foi enviada.")
            return Response({
                "success": False,
                "message": "Nenhuma imagem válida foi enviada."
            }, status=status.HTTP_400_BAD_REQUEST)

        vector = process_faces_with_face_recognition(frames)
        if not vector:
            print("Nenhum rosto detectado nos frames.")
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
    
#DELETE
class FaceDeleteView(DestroyAPIView):
    queryset = Face.objects.all()
    serializer_class = FaceSerializer
    lookup_field = 'id'

#UPDATE
class FaceUpdateView(APIView):
    parser_classes = [MultiPartParser]

    def put(self, request, id):
        files = request.FILES.getlist("frames")

        try:
            face = Face.objects.get(id=id)
        except Face.DoesNotExist:
            return Response({
                "success": False,
                "message": "Face não encontrada."
            }, status=status.HTTP_404_NOT_FOUND)

        if not files:
            return Response({
                "success": False,
                "message": "Frames não enviados."
            }, status=status.HTTP_400_BAD_REQUEST)

        frames = []
        for file in files:
            file_bytes = np.frombuffer(file.read(), np.uint8)
            frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            if frame is not None:
                frames.append(frame)

        vector = process_faces_with_face_recognition(frames)
        if not vector:
            return Response({
                "success": False,
                "message": "Nenhum rosto detectado."
            }, status=status.HTTP_400_BAD_REQUEST)

        face.arr_imagem = vector
        face.save()

        return Response({
            "success": True,
            "face_id": face.id,
            "usuario_id": face.usuario_id
        }, status=status.HTTP_200_OK)
    

SIMILARITY_THRESHOLD = 0.85  # pode ajustar

def comparar_vetores(v1, v2):
    return 1 - cosine(v1, v2)

class FaceValidationView(APIView):
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
            usuario = Usuario.objects.get(pk=id)
            usuario_empresa = UsuarioEmpresa.objects.get(id_usuario=usuario)
            empresa = Empresa.objects.get(pk=id)
        except (Usuario.DoesNotExist, UsuarioEmpresa.DoesNotExist):
            return Response({
                "success": False,
                "message": "Usuário não encontrado."
            }, status=status.HTTP_404_NOT_FOUND)
        
        if usuario.bl_bloqueado:
            return Response({
                "success": False,
                "message": "Usuário bloqueado após múltiplas tentativas. Contate o administrador."
            }, status=status.HTTP_403_FORBIDDEN)

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

        vetor_entrada = process_faces_with_face_recognition(frames)
        if not vetor_entrada:
            return Response({
                "success": False,
                "message": "Nenhum rosto detectado nos frames."
            }, status=status.HTTP_400_BAD_REQUEST)

        faces_salvas = Face.objects.filter(usuario=usuario)

        for face in faces_salvas:
            similaridade = comparar_vetores(vetor_entrada, face.arr_imagem)
            if similaridade >= SIMILARITY_THRESHOLD:
                TentativaAcesso.objects.create(
                    id_usuario_empresa=usuario_empresa,
                    bl_sucesso=True
                )
                registrar_alerta(
                    usuario_empresa=usuario_empresa,
                    tipo_alerta="login_sucesso",
                    mensagem_dict={"mensagem": f"Login facial realizado com sucesso por {usuario.nm_nome}."},
                    enviar_email=True,
                    destinatarios=["jose-vitor_m_silva@estudante.sesisenai.org.br"]
                )
                return Response({
                    "success": True,
                    "autenticado": True,
                    "similaridade": round(similaridade, 3),
                    "usuario_id": usuario.id,
                    "face_id": face.id
                }, status=status.HTTP_200_OK)

        TentativaAcessoAnonimo.objects.create(
            id_empresa=empresa
        )
        registrar_alerta(
            usuario_empresa=usuario_empresa,
            tipo_alerta="login_falha",
            mensagem_dict={"mensagem": f"Tentativa de login facial falhou para {usuario.nm_nome}."},
            enviar_email=True,
            destinatarios=["jose-vitor_m_silva@estudante.sesisenai.org.br"]
        )
        if frames:
            primeiro_frame = frames[0]
            criar_face_anonima(empresa=empresa, frame=primeiro_frame, usuario=usuario)
            
        return Response({
            "success": False,
            "autenticado": False,
            "message": "Nenhuma face compatível encontrada."
        }, status=status.HTTP_401_UNAUTHORIZED)
