import requests
from django.template.loader import render_to_string
from noticias.models import NoticiaImportada
from datetime import datetime, timedelta


def gerar_conteudo_email(disparo, data=None):
    """
    Gera o conteúdo HTML do e-mail com base nas notícias e no layout configurado no disparo.
    
    Parâmetros:
        - disparo: instância do EmailDisparo
        - data: string no formato "YYYY-MM-DD", "YYYY-MM-DD HH:MM", ou "YYYY-MM-DD|YYYY-MM-DD"
    
    Retorno:
        - HTML renderizado com as notícias no intervalo informado
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

    # Busca notícias dentro do intervalo e da categoria
    noticias = NoticiaImportada.objects.filter(
        dt_noticia__range=(data_inicio, data_fim),
        cd_veiculo__id_categoria=disparo.id_categoria.pk
    ).order_by('-dt_noticia')

    # Renderiza o HTML com o template base
    html = render_to_string("emails/components/email_base_render.html", {
        "disparo": disparo,
        "noticias": noticias,
    })

    return html


def enviar_email_mailgrid(destinatarios, assunto, corpo_html):
    """
    Envia um e-mail utilizando a API da Mailgrid.

    Parâmetros:
        - destinatarios: lista de e-mails de destino
        - assunto: título do e-mail
        - corpo_html: conteúdo HTML gerado do e-mail

    Retorna:
        - Dicionário com status e resposta da API
    """

    url = "https://api.mailgrid.net.br/send/"
    
    # ⚠️ Token fixo no código por enquanto
    token = "4747f5ab12120fa83b4a86df6c324c9d"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "emailRemetente": "teste@smrclipping.com.br",     # ⚠️ Use o remetente configurado na Mailgrid
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


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def enviar_email_smtp(destinatarios, assunto, corpo_html):
    """
    Envia um e-mail HTML usando SMTP (Mailgrid).

    Parâmetros:
        - destinatarios: lista de e-mails destino
        - assunto: assunto do e-mail
        - corpo_html: conteúdo HTML do e-mail
    """

    # ⚠️ Você pode mover isso para um .env depois
    smtp_host = "grid331.mailgrid.com.br"
    smtp_port = 587
    smtp_user = "smtp@newsup.app.br"
    smtp_pass = "v8yW98XM7cFI"

    # Cabeçalhos do e-mail
    msg = MIMEMultipart("alternative")
    msg["Subject"] = assunto
    msg["From"] = smtp_user
    msg["To"] = ", ".join(destinatarios)

    # Conteúdo em HTML
    part = MIMEText(corpo_html, "html")
    msg.attach(part)

    try:
        # Envia usando SMTP com TLS
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.sendmail(smtp_user, destinatarios, msg.as_string())

        return {"status": "ok", "mensagem": "E-mail enviado com sucesso via SMTP"}

    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}
