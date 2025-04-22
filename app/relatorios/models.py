from django.db import models
from app.empresas.models import Empresa

class Relatorio(models.Model):
    id = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,  
        related_name='relatorios',     
        null=True,                  
        verbose_name='Empresa'
    )
    tp_relatorio = models.CharField(max_length=50)
    js_conteudo = models.JSONField()
    dt_criado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Relatorio'
        verbose_name_plural = 'Relatorios'
        db_table = 'tb_relatorio'