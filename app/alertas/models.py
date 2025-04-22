from django import models
from app.usuarios_empresas.models import UsuarioEmpresa
class Alerta(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario_empresa = models.ForeignKey(
        UsuarioEmpresa,
        on_delete=models.CASCADE,
        related_name='alertas',
        null=True,
        verbose_name='UsuarioEmpresa'
    )
    tp_alerta = models.CharField(max_length=50)
    js_mensagem = models.JSONField()
    dt_criado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Alerta'
        verbose_name_plural = 'Alertas'
        db_table = 'tb_alerta'
