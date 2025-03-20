from django.utils.timezone import now
from django.db import connection

def registrar_evento(id_cliente=None, usuario=None, descricao=""):
    if not id_cliente:
        print(f"⚠️ ERRO: Evento sem ID de cliente! Descrição: {descricao}")
        return

    if usuario is None or not usuario.is_authenticated:
        print(f"⚠️ ERRO: Evento sem usuário autenticado! Usuário: {usuario}")
        return

    print(f"✔ Registrando evento para Cliente {id_cliente} por {usuario.username}")

    evento = Evento(
        id_cliente_id=id_cliente,
        usuario=usuario,
        descricao=descricao
    )
    evento.save()

def detectar_alteracoes(instancia_antiga, instancia_nova):
    """
    Compara um objeto antes e depois de ser salvo para detectar quais campos foram alterados.
    Retorna uma string com os campos alterados e seus valores antigos e novos.
    """
    alteracoes = []

    for field in instancia_nova._meta.fields:
        nome_campo = field.name
        valor_antigo = getattr(instancia_antiga, nome_campo, None)
        valor_novo = getattr(instancia_nova, nome_campo, None)

        # 🔥 Se o valor foi alterado, adicionamos na lista de mudanças
        if valor_antigo != valor_novo:
            alteracoes.append(f"{nome_campo}: '{valor_antigo}' → '{valor_novo}'")

    return ", ".join(alteracoes) if alteracoes else None
