from rest_framework import generics
from app.relatorios.models import Relatorio
from app.relatorios.serializers import RelatorioSerializer


class RelatoriosAPIView(generics.ListCreateAPIView):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer

class RelatorioAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer
