from rest_framework import generics
from app.usuarios_empresas.models import UsuarioEmpresa
from app.usuarios_empresas.serializers import UsuarioEmpresaSerializer

class UsuariosEmpresaAPIView(generics.ListCreateAPIView):
    queryset = UsuarioEmpresa.objects.select_related('usuario', 'empresa').all()
    serializer_class = UsuarioEmpresaSerializer

class UsuarioEmpresaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsuarioEmpresa.objects.select_related('usuario', 'empresa').all()
    serializer_class = UsuarioEmpresaSerializer

class UsuariosEmpresaPorEmpresaView(generics.ListAPIView):
    serializer_class = UsuarioEmpresaSerializer

    def get_queryset(self):
        empresa_id = self.request.query_params.get('empresa_id')
        if not empresa_id:
            return UsuarioEmpresa.objects.none()

        try:
            empresa_id = int(empresa_id)
        except ValueError:
            return UsuarioEmpresa.objects.none()

        return UsuarioEmpresa.objects.filter(
            empresa__id=empresa_id
        ).order_by('usuario__nm_nome')