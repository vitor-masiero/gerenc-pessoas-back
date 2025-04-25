from app.empresas.models import Empresa
from app.usuarios.models import Usuario
from app.usuarios_empresas.models import UsuarioEmpresa
from rest_framework import serializers
from app.empresas.serializers import EmpresaSerializer
from app.usuarios.serializers import UsuarioSerializer

class UsuarioEmpresaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(),
        source='id',
        required=False,
        write_only=True
    )

    empresa = EmpresaSerializer(read_only=True)
    empresa_id = serializers.PrimaryKeyRelatedField(
        queryset=Empresa.objects.all(),
        source='id',
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
        fields = '__all__'
    
    def create(self, validated_data):
        return UsuarioEmpresa.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    