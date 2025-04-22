from app.alertas.models import Alerta
from rest_framework import serializers

class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = '__all__'
        extra_kwargs = {
            'tp_alerta':{
                'required':True
            },
            'js_mensagem': {
                'required': True
            }
        }