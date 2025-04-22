from django.urls import path
from app.empresas.views import EmpresaAPIView, EmpresasAPIView

urlpatterns = [
    path('', EmpresasAPIView.as_view(), name='endereco-list-create'),
    path('<int:pk>/', EmpresaAPIView.as_view(), name='endereco-detail'),
]