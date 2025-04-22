from django.urls import path
from app.enderecos.views import EnderecosAPIView, EnderecoAPIView

urlpatterns = [
    path('', EnderecosAPIView.as_view(), name='endereco-list-create'),
    path('<int:pk>/', EnderecoAPIView.as_view(), name='endereco-detail'),
]