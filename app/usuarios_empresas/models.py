from django.db import models
from app.usuarios.models import Usuario
from app.enderecos.models import Endereco

class UsuarioEmpresa(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,  
        related_name='usuariosempresa',     
        null=True,                  
        verbose_name='Usuario'
    )
    empresa = models.ForeignKey(
        Empresa, 
        on_delete=models.CASCADE,  
        related_name='usuariosempresas',     
        null=True,                  
        verbose_name='Empresa'
    )
    ds_usuario_permissao = models.CharField(max_length=20)