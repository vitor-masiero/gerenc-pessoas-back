from django.urls import path
from app.tentativas_acesso.views import TentativaAcessoAPIView, TentativasAcessoAPIView

urlpatterns = [
    path('', TentativasAcessoAPIView.as_view(), name='usuario_empresa_list'),
    path('<int:pk>/', TentativaAcessoAPIView.as_view(), name='endereco-detail'),
]