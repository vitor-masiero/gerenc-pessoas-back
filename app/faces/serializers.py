from rest_framework import serializers
from .models import Face

class FaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Face
        fields = ['id', 'usuario', 'arr_imagem', 'dt_criado']
        read_only_fields = ['id', 'dt_criado']