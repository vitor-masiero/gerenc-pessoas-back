from django.core.mail import send_mail
from app.alertas.models import Alerta

def registrar_alerta(usuario_empresa, tipo_alerta, mensagem_dict, enviar_email=False, destinatarios=None):
    """
    Cria um alerta no banco e opcionalmente envia e-mail.
    """
    alerta = Alerta.objects.create(
        id_usuario_empresa=usuario_empresa,
        tp_alerta=tipo_alerta,
        js_mensagem=mensagem_dict
    )

    if enviar_email and destinatarios:
        assunto = f"[{tipo_alerta}] Alerta do sistema"
        corpo = mensagem_dict.get('mensagem', 'Novo alerta gerado.')
        send_mail(
            subject=assunto,
            message=corpo,
            from_email=None
            recipient_list=destinatarios,
            fail_silently=False
        )

    return alerta