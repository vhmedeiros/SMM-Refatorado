# # def cliente_selecionado(request):
# #     return {
# #         "cliente_selecionado": request.session.get("cliente_selecionado")
# #     }

# from clientes.models import ErpCliente
# from configuracoes.models import ConfiguracaoCliente

# def cliente_selecionado(request):
#     cliente_id = request.session.get("cliente_selecionado")
#     cliente = None

#     if cliente_id:
#         try:
#             cliente_obj = ErpCliente.objects.get(id_cliente=cliente_id)
#             config = ConfiguracaoCliente.objects.filter(id_cliente=cliente_obj).first()

#             # Anexamos a sigla ao cliente para facilitar no template
#             if config:
#                 cliente_obj.sigla = config.sigla_cliente
#             cliente = cliente_obj
#         except ErpCliente.DoesNotExist:
#             cliente = None

#     return {
#         "cliente_selecionado": cliente
#     }


from clientes.models import ErpCliente
from configuracoes.models import ConfiguracaoCliente

def cliente_selecionado(request):
    raw = request.session.get("cliente_selecionado")

    # 🧠 Se a sessão tiver só o ID direto (ex: 4627), trata como inteiro
    if isinstance(raw, int):
        cliente_id = raw
    elif isinstance(raw, dict):
        cliente_id = raw.get("id_cliente")
    else:
        cliente_id = None

    if cliente_id:
        try:
            cliente = ErpCliente.objects.get(id_cliente=cliente_id)
            configuracao = ConfiguracaoCliente.objects.filter(id_cliente=cliente).first()
            
            # Injecta a sigla temporariamente (somente para uso no template)
            cliente.sigla = configuracao.sigla_cliente if configuracao else None

            return {"cliente_selecionado": cliente}
        except ErpCliente.DoesNotExist:
            pass

    return {"cliente_selecionado": None}
