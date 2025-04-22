from .models import UsuarioEmpresa, Usuario, Empresa
from rest_framework import serializers
from .serializers import EmpresaSerializer, UsuarioSerializer

class UsuarioEmpresaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(),
        source='id_usuario',
        required=False,
        write_only=True
    )

    empresa = EmpresaSerializer(read_only=True)
    empresa_id = serializers.PrimaryKeyRelatedField(
        queryset=Empresa.objects.all(),
        source='id_empresa',
        required=False,
        write_only=True
    )

    class Meta:
        model = UsuarioEmpresa
        extra_kwargs = {
            'ds_usuario_permissao' : {
                'required' : True,
                'help_text' : 'Permissão do Usuário'
            }
        }
    
    def create(self, validated_data):
        return UsuarioEmpresa.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance