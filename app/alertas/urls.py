from django.urls import path
from app.alertas.views import AlertasAPIView, AlertaAPIView

urlpatterns = [
    path('', AlertasAPIView.as_view(), name='alerta-list-create'),
    path('<int:pk>/', AlertaAPIView.as_view(), name='alerta-detail'),
]