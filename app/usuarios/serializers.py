from rest_framework import serializers
from app.usuarios.models import Usuario
from app.enderecos.models import Endereco
from app.enderecos.serializers import EnderecoSerializer
from django.contrib.auth.hashers import make_password

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
            {'required' : True},
            'dt_bloqueio': {'read_only':True}
        }
    
    def create(self, validated_data):
        endereco = validated_data.pop('id_endereco', None)

        if 'ds_senha_hash' in validated_data:
            validated_data['ds_senha_hash'] = make_password(validated_data['ds_senha_hash'])

        usuario = Usuario.objects.create(**validated_data)
        if endereco:
            usuario.id_endereco = endereco
            usuario.save()
        return usuario

    def update(self, instance, validated_data):
        endereco = validated_data.pop('id_endereco', None)
        if 'ds_senha_hash' in validated_data:
            validated_data['ds_senha_hash'] = make_password(validated_data['ds_senha_hash'])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if endereco:
            instance.id_endereco = endereco
            instance.save()
        return instance

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    senha = serializers.CharField()

class EsqueciSenhaSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ResetarSenhaSerializer(serializers.Serializer):
    email = serializers.EmailField()
    codigo = serializers.CharField()
    nova_senha = serializers.CharField()