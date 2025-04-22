from rest_framework import serializers
from .models import Endereco, Usuario, Empresa, UsuarioEmpresa, Relatorio, TentativaAcesso, TentativaAcessoAnonimo, Alerta, AlertaAnonimo

class TentativaAcessoAnonimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TentativaAcessoAnonimo
        fields = '__all__'

