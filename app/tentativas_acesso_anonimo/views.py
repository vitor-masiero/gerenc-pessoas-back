from rest_framework import generics
from app.tentativas_acesso_anonimo.models import TentativaAcessoAnonimo
from app.tentativas_acesso_anonimo.serializers import TentativaAcessoAnonimoSerializer

class TentativasAcessoAnonimosAPIView(generics.ListCreateAPIView):
    queryset = TentativaAcessoAnonimo.objects.all()
    serializer_class = TentativaAcessoAnonimoSerializer

class TentativaAcessoAnonimoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TentativaAcessoAnonimo.objects.all()
    serializer_class = TentativaAcessoAnonimoSerializer