# # from django.views.generic import TemplateView
# # from django.shortcuts import get_object_or_404, render
# # from django.utils.timezone import timezone, now
# # from noticias.models import NoticiaImportada
# # from configuracoes.models import ConfiguracaoCliente
# # from clientes.models import ErpCliente
# # from datetime import datetime
# # from collections import defaultdict


# # class ClientePaginaPublicaView(TemplateView):
# #     template_name = "site_cliente/noticias.html"

# #     def get_context_data(self, **kwargs):
# #         context = super().get_context_data(**kwargs)

# #         # pega a sigla do cliente que está na URL
# #         sigla = self.kwargs.get('sigla_cliente')

# #         # busca a configuração do cliente
# #         configuracao = get_object_or_404(ConfiguracaoCliente, sigla_cliente__iexact=sigla)
# #         cliente = configuracao.id_cliente

# #         # data que o cliente selecionou o filtro (ou hoje, se não houver filtro)
# #         data_str = self.request.GET.get('data')
# #         if data_str:
# #             try:
# #                 data = datetime.strptime(data_str, '%Y-%m-%d').date()
# #             except ValueError:
# #                 data = now().date()
# #         else:
# #             data = now().date()

# #         noticias = (
# #             NoticiaImportada.objects
# #             .filter(
# #                 clientes_relacionados__contains=str(cliente.id_cliente),
# #                 dt_noticia__year=data.year,
# #                 dt_noticia__month=data.month,
# #                 dt_noticia__day=data.day,
# #                 processado=True,
# #             )
# #             .select_related('cd_veiculo__tipo_veiculo', 'cd_veiculo__cd_uf')
# #             .order_by('cd_veiculo__tipo_veiculo__descricao_tipo_veiculo', 'cd_veiculo__nome_veiculo', '-dt_noticia')
# #         )

# #         # agrupar noticias: tipo veiculo > veiculo > lista noticias
# #         agrupadas = defaultdict(lambda: defaultdict(list))

# #         for noticia in noticias:
# #             tipo = noticia.cd_veiculo.tipo_veiculo.descricao_tipo_veiculo
# #             veiculo = noticia.cd_veiculo.nome_veiculo
# #             agrupadas[tipo][veiculo].append(noticia)

# #         # enviar ao template:
# #         context['configuracao'] = configuracao
# #         context['agrupadas'] = agrupadas
# #         context['data'] = data
# #         context['cliente_selecionado'] = cliente


# #         return context 


# # def pagina_cliente(request, sigla_cliente):
# #     configuracao = get_object_or_404(ConfiguracaoCliente, sigla_cliente=sigla_cliente)
# #     id_cliente = configuracao.id_cliente.id_cliente  # Pegando o ID inteiro

# #     # ⚠️ O campo clientes_relacionados é texto tipo "4627,123", então usamos contains
# #     noticias = NoticiaImportada.objects.filter(
# #         clientes_relacionados__icontains=str(id_cliente)
# #     ).order_by("-dt_noticia")[:100]  # Limite inicial de 100

# #     return render(request, "site_cliente/noticias.html", {
# #         "configuracao": configuracao,
# #         "noticias": noticias,
# #     })

# from django.http import Http404
# from django.shortcuts import get_object_or_404
# from django.utils.timezone import localtime, now
# from django.views.generic import TemplateView
# from noticias.models import NoticiaImportada
# from configuracoes.models import ConfiguracaoCliente

# class ClientePaginaPublicaView(TemplateView):
#     template_name = "site_cliente/noticias.html"

#     def dispatch(self, request, *args, **kwargs):
#         sigla = self.kwargs.get("sigla_cliente")

#         # Busca a configuração ativa pela sigla
#         conf = (
#             ConfiguracaoCliente.objects
#             .select_related("id_cliente")
#             .filter(sigla_cliente__iexact=sigla, status_pagina="A")
#             .first()
#         )

#         if not conf:
#             raise Http404("Página do cliente não encontrada ou inativa.")

#         self.cliente = conf.id_cliente
#         self.config = conf  # se quiser usar o logotipo ou outras configs depois

#         return super().dispatch(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         cliente = self.cliente
#         data = localtime(now()).date()
#         context["data"] = data

#         # Busca todas as notícias do dia processadas
#         todas = (
#             NoticiaImportada.objects
#             .filter(
#                 dt_noticia__date=data,
#                 processado=True,
#             )
#             .select_related('cd_veiculo__tipo_veiculo', 'cd_veiculo__cd_uf')
#             .order_by('cd_veiculo__tipo_veiculo__descricao_tipo_veiculo', 'cd_veiculo__nome_veiculo', '-dt_noticia')
#         )

#         # Filtra apenas as vinculadas ao cliente
#         noticias = [
#             n for n in todas
#             if n.clientes_relacionados and f",{cliente.id_cliente}," in f",{n.clientes_relacionados},"
#         ]

#         # Agrupa por tipo e veículo
#         agrupadas = {}
#         for noticia in noticias:
#             tipo = noticia.cd_veiculo.tipo_veiculo.descricao_tipo_veiculo
#             veiculo = noticia.cd_veiculo.nome_veiculo
#             agrupadas.setdefault(tipo, {}).setdefault(veiculo, []).append(noticia)

#         context["agrupadas"] = agrupadas
#         context["cliente"] = cliente
#         return context


from django.shortcuts import get_object_or_404
from django.utils.timezone import localtime, now
from django.views.generic import TemplateView
from noticias.models import NoticiaImportada
from configuracoes.models import ConfiguracaoCliente

class ClientePaginaPublicaView(TemplateView):
    template_name = "site_cliente/noticias.html"

    def dispatch(self, request, *args, **kwargs):
        sigla = self.kwargs.get("sigla_cliente")

        # Pegamos a configuração com a sigla da URL
        self.config = get_object_or_404(
            ConfiguracaoCliente.objects.select_related("id_cliente"),
            sigla_cliente=sigla,
            status_pagina="A"
        )

        # Guardamos o cliente relacionado
        self.cliente = self.config.id_cliente
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cliente = self.cliente
        config = self.config
        data = localtime(now()).date()

        todas = (
            NoticiaImportada.objects
            .filter(
                dt_noticia__year=data.year,
                dt_noticia__month=data.month,
                dt_noticia__day=data.day,
                processado=True,
            )
            .select_related('cd_veiculo__tipo_veiculo', 'cd_veiculo__cd_uf')
            .order_by('cd_veiculo__tipo_veiculo__descricao_tipo_veiculo', 'cd_veiculo__nome_veiculo', '-dt_noticia')
        )

        noticias = [
            n for n in todas
            if n.clientes_relacionados and f",{cliente.id_cliente}," in f",{n.clientes_relacionados},"
        ]

        agrupadas = {}
        for noticia in noticias:
            tipo = noticia.cd_veiculo.tipo_veiculo.descricao_tipo_veiculo
            veiculo = noticia.cd_veiculo.nome_veiculo
            agrupadas.setdefault(tipo, {}).setdefault(veiculo, []).append(noticia)

        # Adiciona ao contexto
        context.update({
            "agrupadas": agrupadas,
            "data": data,
            "cliente": cliente,
            "config": config,  # <- aqui está o que faltava
        })
        return context
