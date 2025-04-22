from rest_framework import generics
from app.empresas.models import Empresa
from app.empresas.serializers import EmpresaSerializer

class EmpresasAPIView(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpresaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    
