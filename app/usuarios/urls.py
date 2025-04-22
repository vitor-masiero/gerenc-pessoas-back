from django.urls import path
from app.usuarios.views import UsuarioAPIView, UsuariosAPIView

urlpatterns = [
    path('', UsuariosAPIView.as_view(), name='usuario_empresa_list'),
    path('<int:pk>/', UsuarioAPIView.as_view(), name='endereco-detail'),
]