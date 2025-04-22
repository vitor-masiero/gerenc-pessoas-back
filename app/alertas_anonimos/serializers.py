from rest_framework import serializers
from app.alertas_anonimos.models import AlertaAnonimo

class AlertaAnonimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertaAnonimo
        fields = '__all__'
        extra_kwargs = {
            'tp_alerta':{
                'required':True
            },
            'js_mensagem': {
                'required': True
            }
        }