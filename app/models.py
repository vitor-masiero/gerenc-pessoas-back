from django.db import models

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
