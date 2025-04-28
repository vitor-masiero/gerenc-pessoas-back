from django.urls import path
from app.alertas_anonimos.views import AlertasAnonimosAPIView, AlertaAnonimoAPIView, AlertasAnonimosPorEmpresaView

urlpatterns = [
    path('', AlertasAnonimosAPIView.as_view(), name='alerta_anonimo-list-create'),
    path('<int:pk>/', AlertaAnonimoAPIView.as_view(), name='alerta_anonimo-detail'),
    path('empresa/', AlertasAnonimosPorEmpresaView.as_view(), name='alerta_anonimo-por-empresa')
]