from datetime import datetime
from app.usuarios.models import LoginUsuario
from app.relatorios.models import Relatorio

def gerar_relatorio_logins_mensal(empresa_id, ano, mes):
    inicio_mes = datetime(ano, mes, 1)
    if mes == 12:
        fim_mes = datetime(ano + 1, 1, 1)
    else:
        fim_mes = datetime(ano, mes + 1, 1)

    logins = LoginUsuario.objects.filter(
        empresa_id=empresa_id,
        dt_login__gte=inicio_mes,
        dt_login__lt=fim_mes
    )

    total_logins = logins.count()

    conteudo = {
        "empresa_id": empresa_id,
        "mes": f"{mes:02d}/{ano}",
        "total_logins": total_logins
    }

    relatorio = Relatorio.objects.create(
        id_empresa_id=empresa_id,
        tp_relatorio="logins_mensais",
        js_conteudo=conteudo
    )

    return relatorio