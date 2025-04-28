from django.urls import path
from app.alertas.views import AlertasAPIView, AlertaAPIView, AlertasPorEmpresaView

urlpatterns = [
    path('', AlertasAPIView.as_view(), name='alerta-list-create'),
    path('<int:pk>/', AlertaAPIView.as_view(), name='alerta-detail'),
    path('empresa/', AlertasPorEmpresaView.as_view(), name='alertas-por-empresa'),
]