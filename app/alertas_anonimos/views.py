from rest_framework import generics
from app.alertas_anonimos.models import AlertaAnonimo
from app.alertas_anonimos.serializers import AlertaAnonimoSerializer

class AlertasAnonimosAPIView(generics.ListCreateAPIView):
    queryset = AlertaAnonimo.objects.all()
    serializer_class = AlertaAnonimoSerializer

class AlertaAnonimoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlertaAnonimo.objects.all()
    serializer_class = AlertaAnonimoSerializer