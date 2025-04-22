from rest_framework import generics
from .models import UsuarioEmpresa
from .serializers import UsuarioEmpresaSerializer

class UsuariosEmpresaAPIView(generics.ListCreateAPIView):
    queryset = UsuarioEmpresa.objects.all()
    serializer_class = UsuarioEmpresaSerializer

class UsuarioEmpresaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsuarioEmpresa.objects.all()
    serializer_class = UsuarioEmpresaSerializer