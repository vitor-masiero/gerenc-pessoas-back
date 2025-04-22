from rest_framework import serializers
from app.usuarios.models import Usuario
from app.enderecos.models import Endereco
from app.enderecos.serializers import EnderecoSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    id_endereco = EnderecoSerializer(read_only=True)
    id_endereco_id = serializers.PrimaryKeyRelatedField(
        queryset = Endereco.objects.all(),
        source='id_endereco',
        write_only=True,
        required=False
    )
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {
            'nu_cpf' : 
            {'required' : True, 'help_text' : 'Informe um CPF válido'},
            'ds_senha_hash' : 
            {'write_only' : True, 'help_text' : 'Senha do usuário, será armazenada mas não revelada.' },
            'ds_email' : 
            {'required' : True}
        }
    
    def create(self, validated_data):
        endereco = validated_data.pop('id_endereco', None)
        usuario = Usuario.objects.create(**validated_data)
        if endereco:
            usuario.id_endereco = endereco
            usuario.save()
        return usuario

    def update(self, instance, validated_data):
        endereco = validated_data.pop('id_endereco', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if endereco:
            instance.id_endereco = endereco
            instance.save()
        return instance