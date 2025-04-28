from rest_framework import generics
from app.tentativas_acesso.models import TentativaAcesso
from app.tentativas_acesso.serializers import TentativaAcessoSerializer

class TentativasAcessoAPIView(generics.ListCreateAPIView):
    queryset = TentativaAcesso.objects.all()
    serializer_class = TentativaAcessoSerializer

class TentativaAcessoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TentativaAcesso.objects.all()
    serializer_class = TentativaAcessoSerializer

class TentativasAcessoPorEmpresaView(generics.ListAPIView):
    serializer_class = TentativaAcessoSerializer

    def get_queryset(self):
        empresa_id = self.request.query_params.get('empresa_id')
        if not empresa_id:
            return TentativaAcesso.objects.none()

        try:
            empresa_id = int(empresa_id)
        except ValueError:
            return TentativaAcesso.objects.none()

        return TentativaAcesso.objects.filter(
            id_usuario_empresa__empresa__id=empresa_id
        ).order_by('-dt_tentativa')