from rest_framework import generics
from app.tentativas_acesso.models import TentativaAcesso
from app.tentativas_acesso.serializers import TentativaAcessoSerializer

class TentativasAcessoAPIView(generics.ListCreateAPIView):
    queryset = TentativaAcesso.objects.all()
    serializer_class = TentativaAcessoSerializer

class TentativaAcessoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TentativaAcesso.objects.all()
    serializer_class = TentativaAcessoSerializer