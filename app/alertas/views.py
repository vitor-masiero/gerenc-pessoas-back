from rest_framework import generics
from app.alertas.models import Alerta
from app.alertas.serializers import AlertaSerializer

class AlertasAPIView(generics.ListCreateAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer

class AlertaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer

class AlertasPorEmpresaView(generics.ListAPIView):
    serializer_class = AlertaSerializer

    def get_queryset(self):
        empresa_id = self.request.query_params.get('empresa_id')
        if not empresa_id:
            return Alerta.objects.none()

        try:
            empresa_id = int(empresa_id)
        except ValueError:
            return Alerta.objects.none()

        # Aqui precisa fazer JOIN para pegar alertas pela empresa
        return Alerta.objects.filter(id_usuario_empresa__empresa_id=empresa_id).order_by('-dt_criado')