from rest_framework import serializers
from app.tentativas_acesso.models import TentativaAcesso

class TentativaAcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TentativaAcesso
        fields = '__all__'