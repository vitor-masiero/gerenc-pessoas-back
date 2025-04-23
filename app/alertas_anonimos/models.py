from django.db import models
from app.empresas.models import Empresa

class AlertaAnonimo(models.Model):
    id_usuario_empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        related_name='alertasAnonimos',
        null=True,
        verbose_name='Alerta de Acesso Anônimo'
    )
    tp_alerta = models.CharField(max_length=50)
    js_mensagem = models.JSONField()
    dt_criado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Alerta Anônimo'
        verbose_name_plural = 'Alertas Anônimos'
        db_table = 'tb_alerta_anonimo'