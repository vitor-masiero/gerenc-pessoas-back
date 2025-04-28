from rest_framework import generics
from app.alertas_anonimos.models import AlertaAnonimo
from app.alertas_anonimos.serializers import AlertaAnonimoSerializer

class AlertasAnonimosAPIView(generics.ListCreateAPIView):
    queryset = AlertaAnonimo.objects.all()
    serializer_class = AlertaAnonimoSerializer

class AlertaAnonimoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlertaAnonimo.objects.all()
    serializer_class = AlertaAnonimoSerializer

class AlertasAnonimosPorEmpresaView(generics.ListAPIView):
    serializer_class = AlertaAnonimoSerializer

    def get_queryset(self):
        empresa_id = self.request.query_params.get('empresa_id')
        if not empresa_id:
            return AlertaAnonimo.objects.none()
        
        try:
            empresa_id = int(empresa_id)
        except ValueError:
            return AlertaAnonimo.objects.none()
        
        return AlertaAnonimo.objects.filter(id_empresa_id=empresa_id).order_by('-dt_criado')