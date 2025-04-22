from django.db import models
from app.empresas.models import Empresa

class TentativaAcessoAnonimo(models.Model):
    id_empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,  
        related_name='tentativasAcessoAnonimos',     
        null=True,                  
        verbose_name='Empresa'
    )
    dt_tentativa = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Tentativa Acesso Anonimo'
        verbose_name_plural = 'Tentativas de Acesso Anonimo'
        db_table = 'tb_tentativa_acesso_anonimo'
