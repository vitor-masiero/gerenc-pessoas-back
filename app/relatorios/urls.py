from django.urls import path
from app.relatorios.views import RelatorioAPIView, RelatoriosAPIView

urlpatterns = [
    path('', RelatoriosAPIView.as_view(), name='relatorio-list-create'),
    path('<int:pk>/', RelatorioAPIView.as_view(), name='relatorio-detail'),
]