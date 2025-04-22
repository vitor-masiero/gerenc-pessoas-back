from django.db import models
from django.contrib.postgres.fields import ArrayField
from app.usuarios.models import Usuario

class Face(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,  
        related_name='faces',     
        null=True,                  
        verbose_name='Usuario'
    )
    arr_imagem = ArrayField(models.FloatField()) #Não sobrecarrega o Banco
    dt_criado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Face'
        verbose_name_plural = 'Faces'
        db_table = 'tb_face'