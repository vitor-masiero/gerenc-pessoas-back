from rest_framework import generics
from app.alertas.models import Alerta
from app.alertas.serializers import AlertaSerializer

class AlertasAPIView(generics.ListCreateAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer

class AlertaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer