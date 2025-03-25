from django.shortcuts import get_object_or_404
from clientes.models import ErpCliente
import re

class ClienteSelecionadoMiddleware:
    """
    Middleware para verificar se um cliente foi selecionado via sessão
    ou presente na URL como /cliente/<id_cliente>/ e colocá-lo no request.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        cliente = None

        # Verifica se há cliente na sessão
        cliente_id = request.session.get('cliente_selecionado_id')
        if cliente_id:
            try:
                cliente = ErpCliente.objects.get(id_cliente=cliente_id)
            except ErpCliente.DoesNotExist:
                cliente = None

        # Se não houver na sessão, tenta capturar da URL (por regex)
        if not cliente:
            match = re.search(r'/cliente/(?P<id_cliente>\d+)', request.path)
            if match:
                cliente_id_url = match.group('id_cliente')
                try:
                    cliente = ErpCliente.objects.get(id_cliente=cliente_id_url)
                    request.session['cliente_selecionado_id'] = cliente.id_cliente
                except ErpCliente.DoesNotExist:
                    cliente = None

        request.cliente_selecionado = cliente
        response = self.get_response(request)
        return response
