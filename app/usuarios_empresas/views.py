from rest_framework import generics
from app.usuarios_empresas.models import UsuarioEmpresa
from app.usuarios_empresas.serializers import UsuarioEmpresaSerializer

class UsuariosEmpresaAPIView(generics.ListCreateAPIView):
    queryset = UsuarioEmpresa.objects.select_related('usuario', 'empresa').all()
    serializer_class = UsuarioEmpresaSerializer

class UsuarioEmpresaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsuarioEmpresa.objects.select_related('usuario', 'empresa').all()
    serializer_class = UsuarioEmpresaSerializer