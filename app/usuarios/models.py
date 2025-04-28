from django.db import models
from django.utils import timezone
from app.enderecos.models import Endereco
from app.empresas.models import Empresa

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nm_nome = models.CharField(max_length=100)
    ds_email = models.EmailField(unique=True)
    nu_telefone = models.CharField(max_length=15, blank=True, null=True)
    nu_cpf = models.CharField(max_length=15)
    id_endereco = models.ForeignKey(
        Endereco, 
        on_delete=models.SET_NULL,  # Não exclui o usuário se o endereço for excluído
        related_name='usuarios',     # Para acessar usuários a partir do endereço
        null=True,                  # Permite que o usuário não tenha endereço
        verbose_name='Endereço'
    )
    ds_senha_hash = models.CharField(max_length=200)
    bl_bloqueado = models.BooleanField(default=False)
    nu_tentativas_falhas = models.IntegerField(default=0)
    dt_bloqueio = models.DateTimeField(null=True, blank=True)
    cd_recuperacao_senha = models.CharField(max_length=6, null=True, blank=True)
    dt_codigo_expiracao = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk:
            # Obtém o registro anterior para comparar o valor de bl_bloqueado
            old = Usuario.objects.get(pk=self.pk)
            if not old.bl_bloqueado and self.bl_bloqueado:
                self.dt_bloqueio = timezone.now()
        else:
            # Caso o usuário já seja criado como bloqueado
            if self.bl_bloqueado and not self.dt_bloqueio:
                self.dt_bloqueio = timezone.now()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['nm_nome']
        db_table = 'tb_usuario'
    
    def __str__(self):
        return f"{self.nm_nome} ({self.ds_email})"


class LoginUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='logins')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='logins')
    dt_login = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Login de Usuário'
        verbose_name_plural = 'Logins de Usuários'
        db_table = 'tb_login_usuario'