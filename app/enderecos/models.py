from django.db import models

class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    nu_cep = models.CharField(max_length=9)  # Formato: 00000-000
    nm_logradouro = models.CharField(max_length=100)  # Rua, Avenida, etc.
    nu_numero = models.CharField(max_length=20)  # CharField para permitir valores como "s/n"
    ds_complemento = models.CharField(max_length=100, blank=True, null=True)
    nm_bairro = models.CharField(max_length=50)
    nm_cidade = models.CharField(max_length=50)
    sg_estado = models.CharField(max_length=2)
    nm_pais = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['nm_pais','nm_cidade', 'sg_estado', 'nm_bairro', 'nm_logradouro']  # Ordem padrão
        db_table = 'tb_endereco'  # Nome personalizado da tabela no DB
    
    def _str_(self):
        return f"{self.logradouro}, {self.numero}\n{self.bairro}\n{self.cidade}/{self.estado}\n{self.cep}"
