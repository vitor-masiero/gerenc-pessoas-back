from django.urls import path
from app.alertas_anonimos.views import AlertasAnonimosAPIView, AlertaAnonimoAPIView

urlpatterns = [
    path('', AlertasAnonimosAPIView.as_view(), name='alerta_anonimo-list-create'),
    path('<int:pk>/', AlertaAnonimoAPIView.as_view(), name='alerta_anonimo-detail'),
]