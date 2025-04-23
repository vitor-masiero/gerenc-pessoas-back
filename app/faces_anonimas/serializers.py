from rest_framework import serializers
from app.faces_anonimas.models import FaceAnonima

class FaceAnonimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceAnonima
        fields = ['id', 'id_tentativa_acesso_anonimo', 'img_anonimo', 'dt_criado']
        read_only_fields = ['id', 'dt_criado']