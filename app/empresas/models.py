from django.db import models
from app.enderecos.models import Endereco

class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    id_endereco = models.ForeignKey(
        Endereco, 
        on_delete=models.SET_NULL,  
        related_name='empresas',     
        null=True,                  
        verbose_name='Endereço'
    )
    nm_nome = models.CharField(max_length=100)
    ds_cnpj = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        db_table = 'tb_empresa'
    
    def _str_(self):
        return f"{self.nm_nome} - {self.ds_cnpj}"