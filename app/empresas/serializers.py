from rest_framework import serializers
from app.enderecos.models import Endereco
from app.empresas.models import Empresa
from app.enderecos.serializers import EnderecoSerializer

class EmpresaSerializer(serializers.ModelSerializer):
    id_endereco = EnderecoSerializer(read_only=True)
    id_endereco_id = serializers.PrimaryKeyRelatedField(
        queryset=Endereco.objects.all(),
        source='id_endereco',
        write_only=True,
        required='False'
    )
    class Meta:
        model = Empresa
        fields = '__all__'
        extra_kwargs = {
            'nm_nome': {
                'required':True,
                'help_text':'Nome da empresa'
            },
            'ds_cnpj': {
                'required':True,
                'help_text': 'CNPJ da empresa'
            },
            'ds_senha_hash':  {
                'required':True,
                'write_only': True,
                'help_text': 'Senha da empresa.'
            }
        }
    
    def create(self, validated_data):
        endereco = validated_data.pop('id_endereco', None)
        empresa = Empresa.objects.create(**validated_data)
        if endereco:
            empresa.id_endereco = endereco
            empresa.save()
        return empresa
    
    def update(self, instance, validated_data):
        endereco = validated_data.pop('id_endereco', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if endereco:
            instance.id_endereco = endereco
            instance.save()
        return instance
