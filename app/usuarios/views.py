from rest_framework import generics
from app.usuarios.models import Usuario, LoginUsuario
from app.usuarios.serializers import UsuarioSerializer, LoginSerializer, EsqueciSenhaSerializer, ResetarSenhaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password, make_password
from django.core.mail import send_mail
from random import randint
from django.utils import timezone
from servidor import settings
from app.usuarios_empresas.models import UsuarioEmpresa
from app.empresas.models import Empresa

#Métodos genéricos - CRUD
class UsuariosAPIView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
class UsuarioAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer()

#Métodos extras - Login de Usuário e Desbloqueio
class UsuarioLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            senha = serializer.validated_data['senha']
            empresa_id = serializer.validated_data.get('empresa_id')

            try:
                usuario = Usuario.objects.get(ds_email=email)
            except Usuario.DoesNotExist:
                return Response({"erro": "Email ou senha inválidos."}, status=status.HTTP_401_UNAUTHORIZED)

            if usuario.bl_bloqueado:
                return Response({"erro": "Usuário bloqueado."}, status=status.HTTP_403_FORBIDDEN)

            if not check_password(senha, usuario.ds_senha_hash):
                usuario.nu_tentativas_falhas += 1

                if usuario.nu_tentativas_falhas >= 3:
                    usuario.bl_bloqueado = True
                
                usuario.save()
                
                return Response({"erro": "Email ou senha inválidos."}, status=status.HTTP_401_UNAUTHORIZED)
            
            # Senha correta
            usuario.nu_tentativas_falhas = 0
            usuario.save()

            permissoes = []
            for ue in UsuarioEmpresa.objects.filter(usuario=usuario):
                permissoes.append({
                    "empresa_id": ue.empresa.id,
                    "permissao": ue.ds_usuario_permissao
                })

            if not empresa_id:
                return Response({"erro": "Empresa não informada."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                empresa = Empresa.objects.get(id=empresa_id)
            except Empresa.DoesNotExist:
                return Response({"erro": "Empresa não encontrada."}, status=status.HTTP_404_NOT_FOUND)

            # Verificar se o usuário pertence à empresa
            if not UsuarioEmpresa.objects.filter(usuario=usuario, empresa=empresa).exists():
                return Response({"erro": "Usuário não pertence a essa empresa."}, status=status.HTTP_403_FORBIDDEN)

            # Criar log de login
            LoginUsuario.objects.create(usuario=usuario, empresa=empresa)

            return Response({
                "mensagem": "Login realizado com sucesso!",
                "usuario_id": usuario.id,
                "nome": usuario.nm_nome,
                "email": usuario.ds_email,
                "empresa_id": empresa.id,
                "permissão":permissoes
            }, status=status.HTTP_200_OK)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Desbloqueio manual do usuários
class DesbloquearUsuarioView(APIView):
    def post(self, request, pk):
        try:
            usuario = Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            return Response({"erro": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        usuario.bl_bloqueado = False
        usuario.nu_tentativas_falhas = 0
        usuario.dt_bloqueio = None
        usuario.save()

        return Response({"mensagem": "Usuário desbloqueado com sucesso."}, status=status.HTTP_200_OK)
    
#Esqueci minha senha:
class EsqueciSenhaView(APIView):
    def post(self, request):
        serializer = EsqueciSenhaSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']

            try:
                usuario = Usuario.objects.get(ds_email=email)
            except Usuario.DoesNotExist:
                return Response({"erro": "Email não encontrado."}, status=status.HTTP_404_NOT_FOUND)

            codigo = f"{randint(100000, 999999)}"
            usuario.cd_recuperacao_senha = codigo
            usuario.dt_codigo_expiracao = timezone.now() + timezone.timedelta(minutes=30)
            usuario.save()

            # Envia o código por e-mail
            send_mail(
                subject='Recuperação de Senha',
                message=f'Seu código de recuperação é: {codigo}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[usuario.ds_email],
                fail_silently=False,
            )

            return Response({"mensagem": "Código de recuperação enviado para o e-mail."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Resetar a senha:
class ResetarSenhaView(APIView):
    def post(self, request):
        serializer = ResetarSenhaSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            codigo = serializer.validated_data['codigo']
            nova_senha = serializer.validated_data['nova_senha']

            try:
                usuario = Usuario.objects.get(ds_email=email)
            except Usuario.DoesNotExist:
                return Response({"erro": "Email não encontrado."}, status=status.HTTP_404_NOT_FOUND)

            # Validar código e expiração
            if (usuario.cd_recuperacao_senha != codigo or
                usuario.dt_codigo_expiracao is None or
                usuario.dt_codigo_expiracao < timezone.now()):
                return Response({"erro": "Código inválido ou expirado."}, status=status.HTTP_400_BAD_REQUEST)

            # Atualizar senha
            usuario.ds_senha_hash = make_password(nova_senha)
            usuario.cd_recuperacao_senha = None
            usuario.dt_codigo_expiracao = None
            usuario.save()

            return Response({"mensagem": "Senha alterada com sucesso!"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
