from django.urls import path
from app.tentativas_acesso.views import TentativaAcessoAPIView, TentativasAcessoAPIView, TentativasAcessoPorEmpresaView

urlpatterns = [
    path('', TentativasAcessoAPIView.as_view(), name='usuario_empresa_list'),
    path('<int:pk>/', TentativaAcessoAPIView.as_view(), name='endereco-detail'),
    path('empresa/', TentativasAcessoPorEmpresaView.as_view(), name='tentativas-acesso-por-empresa'),
]