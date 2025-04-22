from django.db import models
from app.tentativas_acesso_anonimo.models import TentativaAcessoAnonimo

class FaceAnonima(models.Model):
    id_tentativa_acesso_anonimo = models.ForeignKey(
        TentativaAcessoAnonimo,
        on_delete=models.CASCADE,  
        related_name='facesanonimas',     
        null=True,                  
        verbose_name='Tentativa de Acesso Anonimo'
    )
    img_anonimo = models.ImageField(upload_to='img_anonimas/')
    dt_criado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Face Anonimas'
        verbose_name_plural = 'Faces Anonimas'
        db_table = 'tb_face_anonima' 