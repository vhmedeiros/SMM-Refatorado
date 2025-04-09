from decouple import config
import requests
from django.template.loader import render_to_string
from noticias.models import NoticiaImportada
from datetime import datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def gerar_conteudo_email(disparo, data=None):
    """
    Gera o conteúdo HTML do e-mail com base nas notícias e no layout configurado no disparo.
    """
    data_inicio = None
    data_fim = None

    if data:
        if '|' in data:
            partes = data.split('|')
            data_inicio = datetime.strptime(partes[0].strip(), "%Y-%m-%d")
            data_fim = datetime.strptime(partes[1].strip(), "%Y-%m-%d") + timedelta(days=1)
        else:
            data_inicio = datetime.strptime(data.strip(), "%Y-%m-%d")
            data_fim = data_inicio + timedelta(days=1)
    else:
        data_fim = datetime.now()
        data_inicio = data_fim - timedelta(days=1)

    noticias = NoticiaImportada.objects.filter(
        dt_noticia__range=(data_inicio, data_fim),
        cd_veiculo__id_categoria=disparo.id_categoria.pk
    ).order_by('-dt_noticia')

    html = render_to_string("emails/components/email_base_render.html", {
        "disparo": disparo,
        "noticias": noticias,
    })

    return html


def enviar_email_mailgrid(destinatarios, assunto, corpo_html):
    """
    Envia um e-mail utilizando a API da Mailgrid.
    """
    url = "https://api.mailgrid.net.br/send/"
    token = config("MAILGRID_TOKEN")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "emailRemetente": "teste@smrclipping.com.br",
        "nomeRemetente": "SMR Clipping",
        "emailDestino": destinatarios,
        "assunto": assunto,
        "mensagem": corpo_html,
        "mensagemTipo": "html",
        "mensagemEncoding": "quoted-printable",
        "mensagemAlt": "Visualize esta mensagem em um cliente que suporte HTML"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return {
                "status": "ok",
                "resposta": response.json()
            }
        else:
            return {
                "status": "erro",
                "codigo": response.status_code,
                "mensagem": response.text
            }

    except requests.exceptions.RequestException as e:
        return {
            "status": "erro",
            "mensagem": f"Erro de conexão com Mailgrid: {str(e)}"
        }


def enviar_email_smtp(destinatarios, assunto, corpo_html):
    """
    Envia um e-mail HTML usando SMTP (Mailgrid).
    """
    smtp_host = config("SMTP_HOST")
    smtp_port = config("SMTP_PORT", cast=int)  # Cast para garantir que seja inteiro
    smtp_user = config("SMTP_USER")
    smtp_pass = config("SMTP_PASS")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = assunto
    msg["From"] = smtp_user
    msg["To"] = ", ".join(destinatarios)

    part = MIMEText(corpo_html, "html")
    msg.attach(part)

    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.sendmail(smtp_user, destinatarios, msg.as_string())

        return {"status": "ok", "mensagem": "E-mail enviado com sucesso via SMTP"}

    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}
