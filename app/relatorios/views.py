from rest_framework import generics
from app.relatorios.models import Relatorio
from app.relatorios.serializers import RelatorioSerializer
from app.relatorios.services import gerar_relatorio_logins_mensal
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RelatoriosAPIView(generics.ListCreateAPIView):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer

class RelatorioAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer

class GerarRelatorioLoginView(APIView):
    def post(self, request):
        empresa_id = request.data.get('empresa_id')
        ano = request.data.get('ano')
        mes = request.data.get('mes')

        if not all([empresa_id, ano, mes]):
            return Response({"erro": "Empresa, ano e mês são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

        relatorio = gerar_relatorio_logins_mensal(empresa_id, int(ano), int(mes))

        return Response({
            "mensagem": "Relatório gerado com sucesso!",
            "relatorio_id": relatorio.id
        }, status=status.HTTP_201_CREATED)

class RelatoriosPorEmpresaView(generics.ListAPIView):
    serializer_class = RelatorioSerializer

    def get_queryset(self):
        empresa_id = self.request.query_params.get('empresa_id')
        if not empresa_id:
            return Relatorio.objects.none()
        
        try:
            empresa_id = int(empresa_id)
        except ValueError:
            return Relatorio.objects.none()
        
        return Relatorio.objects.filter(id_empresa_id=empresa_id).order_by('-dt_criado')