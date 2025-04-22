from .models import Relatorio
from rest_framework import serializers

class RelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relatorio
        fields = '__all__'
        extra_kwargs = {
            'tp_relatorio': {
                'required' : True
            },
            'js_conteudo' : {   
                'required' : True
            }
        }