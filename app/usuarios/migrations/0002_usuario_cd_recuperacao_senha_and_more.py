# Generated by Django 5.1.8 on 2025-04-27 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cd_recuperacao_senha',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='dt_codigo_expiracao',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
