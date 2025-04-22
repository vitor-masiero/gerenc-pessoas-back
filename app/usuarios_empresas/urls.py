from django.urls import path
from app.usuarios_empresas.views import UsuariosEmpresaAPIView, UsuarioEmpresaAPIView

urlpatterns = [
    path('', UsuariosEmpresaAPIView.as_view(), name='relatorio-list-create'),
    path('<int:pk>/', UsuarioEmpresaAPIView.as_view(), name='relatorio-detail'),
]