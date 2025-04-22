from django.db import models
from app.usuarios_empresas.models import UsuarioEmpresa

class TentativaAcesso(models.Model):
    id_usuario_empresa = models.ForeignKey(
        UsuarioEmpresa,
        on_delete=models.CASCADE,
        related_name='tentativasAcesso',
        null=True,
        verbose_name='UsuarioEmpresa'
    )
    dt_tentativa = models.DateTimeField(auto_now_add=True)
    bl_sucesso = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Tentativa de Acesso'
        verbose_name_plural = 'Tentativas de Acesso'
        db_table = 'tb_tentativa_acesso'
