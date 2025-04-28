from django.urls import path
from app.usuarios_empresas.views import UsuariosEmpresaAPIView, UsuarioEmpresaAPIView, UsuariosEmpresaPorEmpresaView

urlpatterns = [
    path('', UsuariosEmpresaAPIView.as_view(), name='relatorio-list-create'),
    path('<int:pk>/', UsuarioEmpresaAPIView.as_view(), name='relatorio-detail'),
    path('empresa/', UsuariosEmpresaPorEmpresaView.as_view())
]