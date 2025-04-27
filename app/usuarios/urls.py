from django.urls import path
from app.usuarios.views import UsuarioAPIView, UsuariosAPIView, UsuarioLoginView, DesbloquearUsuarioView, EsqueciSenhaView, ResetarSenhaView

urlpatterns = [
    path('', UsuariosAPIView.as_view(), name='usuario_empresa_list'),
    path('<int:pk>/', UsuarioAPIView.as_view(), name='endereco-detail'),
    path('login/', UsuarioLoginView.as_view(), name='login'),
    path('<int:pk>/desbloquear',DesbloquearUsuarioView.as_view(), name='desbloquear-user'),
    path('esqueci-senha/', EsqueciSenhaView.as_view(), name='esqueci_senha'),
    path('resetar-senha/', ResetarSenhaView.as_view(), name='resetar_senha'),
]