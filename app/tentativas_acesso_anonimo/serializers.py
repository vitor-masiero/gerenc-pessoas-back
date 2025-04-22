from rest_framework import serializers
from app.tentativas_acesso_anonimo.models import TentativaAcessoAnonimo

class TentativaAcessoAnonimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TentativaAcessoAnonimo
        fields = '__all__'

