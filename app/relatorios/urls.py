from django.urls import path
from app.relatorios.views import RelatorioAPIView, RelatoriosAPIView, GerarRelatorioLoginView, RelatoriosPorEmpresaView

urlpatterns = [
    path('', RelatoriosAPIView.as_view(), name='relatorio-list-create'),
    path('<int:pk>/', RelatorioAPIView.as_view(), name='relatorio-detail'),
    path('gerar-relatorio/', GerarRelatorioLoginView.as_view(), name='gerar-relatorios'),
    path('empresa/', RelatoriosPorEmpresaView.as_view(), name='relatorios-por-empresa')
]