from django.urls import path
from app.tentativas_acesso_anonimo.views import TentativaAcessoAnonimoAPIView, TentativasAcessoAnonimosAPIView, TentativaAcessoAnonimoPorEmpresaAPIView

urlpatterns = [
    path('', TentativasAcessoAnonimosAPIView.as_view(), name='tentativa_acesso_anonimo-list'),
    path('<int:pk>/', TentativaAcessoAnonimoAPIView.as_view(), name='tentativa_acesso_anonimo-details'),
    path('empresa/', TentativaAcessoAnonimoPorEmpresaAPIView.as_view())

]