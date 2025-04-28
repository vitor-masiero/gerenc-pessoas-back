from rest_framework import generics
from app.tentativas_acesso_anonimo.models import TentativaAcessoAnonimo
from app.tentativas_acesso_anonimo.serializers import TentativaAcessoAnonimoSerializer

class TentativasAcessoAnonimosAPIView(generics.ListCreateAPIView):
    queryset = TentativaAcessoAnonimo.objects.all()
    serializer_class = TentativaAcessoAnonimoSerializer

class TentativaAcessoAnonimoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TentativaAcessoAnonimo.objects.all()
    serializer_class = TentativaAcessoAnonimoSerializer

class TentativaAcessoAnonimoPorEmpresaAPIView(generics.ListAPIView):
    serializer_class = TentativaAcessoAnonimoSerializer

    def get_queryset(self):
        empresa_id = self.request.query_params.get('empresa_id')
        if not empresa_id:
            return TentativaAcessoAnonimo.objects.none()
        
        try:
            empresa_id = int(empresa_id)
        except ValueError:
            return TentativaAcessoAnonimo.objects.none()
        
        return TentativaAcessoAnonimo.objects.filter(id_empresa_id=empresa_id)