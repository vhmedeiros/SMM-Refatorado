# from django.shortcuts import get_object_or_404
# from django.utils.timezone import localtime, now
# from django.views.generic import TemplateView
# from noticias.models import NoticiaImportada
# from configuracoes.models import ConfiguracaoCliente
# from vinculos_clientes_noticias.models import VinculoNoticiaClienteCategoria

# class ClientePaginaPublicaView(TemplateView):
#     template_name = "site_cliente/noticias.html"

#     def dispatch(self, request, *args, **kwargs):
#         sigla = self.kwargs.get("sigla_cliente")

#         self.config = get_object_or_404(
#             ConfiguracaoCliente.objects.select_related("id_cliente"),
#             sigla_cliente=sigla,
#             status_pagina="A"
#         )
#         self.cliente = self.config.id_cliente
#         return super().dispatch(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         cliente = self.cliente
#         config = self.config
#         request = self.request

#         from datetime import datetime
#         data_str = request.GET.get("data")
#         if data_str:
#             try:
#                 data = datetime.strptime(data_str, "%Y-%m-%d").date()
#             except ValueError:
#                 data = localtime(now()).date()
#         else:
#             data = localtime(now()).date()

#         context["data"] = data

#         # IDs de notícias vinculadas a este cliente para a data
#         ids_vinculadas = VinculoNoticiaClienteCategoria.objects.filter(
#             id_cliente=cliente.id_cliente,
#             cd_noticia__dt_noticia__date=data
#         ).values_list("cd_noticia", flat=True)

#         noticias = (
#             NoticiaImportada.objects
#             .filter(cd_noticia__in=ids_vinculadas)
#             .select_related("cd_veiculo__tipo_veiculo", "cd_veiculo__cd_uf")
#             .order_by("cd_veiculo__tipo_veiculo__descricao_tipo_veiculo", "cd_veiculo__nome_veiculo", "-dt_noticia")
#         )

#         agrupadas = {}
#         for noticia in noticias:
#             tipo = noticia.cd_veiculo.tipo_veiculo.descricao_tipo_veiculo
#             veiculo = noticia.cd_veiculo.nome_veiculo

#             # 🔹 Categorias vinculadas a essa notícia e cliente
#             categorias = VinculoNoticiaClienteCategoria.objects.filter(
#                 cd_noticia=noticia,
#                 id_cliente=cliente
#             ).select_related('id_categoria')

#             noticia.categorias_cliente = [v.id_categoria.nome for v in categorias]

#             agrupadas.setdefault(tipo, {}).setdefault(veiculo, []).append(noticia)

#         context.update({
#             "agrupadas": agrupadas,
#             "cliente": cliente,
#             "config": config,
#         })
#         return context

from django.shortcuts import get_object_or_404
from django.utils.timezone import localtime, now
from django.views.generic import TemplateView
from noticias.models import NoticiaImportada
from configuracoes.models import ConfiguracaoCliente
from vinculos_clientes_noticias.models import VinculoNoticiaClienteCategoria

class ClientePaginaPublicaView(TemplateView):
    template_name = "site_cliente/noticias.html"

    def dispatch(self, request, *args, **kwargs):
        sigla = self.kwargs.get("sigla_cliente")

        self.config = get_object_or_404(
            ConfiguracaoCliente.objects.select_related("id_cliente"),
            sigla_cliente=sigla,
            status_pagina="A"
        )
        self.cliente = self.config.id_cliente
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cliente = self.cliente
        config = self.config
        request = self.request

        from datetime import datetime
        data_str = request.GET.get("data")
        tipo_veiculo = request.GET.get("tipo")

        if data_str:
            try:
                data = datetime.strptime(data_str, "%Y-%m-%d").date()
            except ValueError:
                data = localtime(now()).date()
        else:
            data = localtime(now()).date()

        context["data"] = data
        context["tipo_veiculo_selecionado"] = tipo_veiculo

        # Vinculações filtradas
        vinculacoes = VinculoNoticiaClienteCategoria.objects.filter(
            id_cliente=cliente.id_cliente,
            cd_noticia__dt_noticia__date=data
        ).select_related(
            "cd_noticia", "cd_noticia__cd_veiculo",
            "cd_noticia__cd_veiculo__tipo_veiculo",
            "cd_noticia__cd_veiculo__cd_uf",
            "id_categoria"
        )

        if tipo_veiculo:
            vinculacoes = vinculacoes.filter(cd_noticia__cd_veiculo__tipo_veiculo__descricao_tipo_veiculo=tipo_veiculo)

        agrupadas = {}
        noticias_vistas = {}

        for v in vinculacoes:
            noticia = v.cd_noticia
            noticia_id = noticia.cd_noticia

            tipo = noticia.cd_veiculo.tipo_veiculo.descricao_tipo_veiculo
            veiculo = noticia.cd_veiculo.nome_veiculo

            if noticia_id not in noticias_vistas:
                noticia.categorias_cliente = [v.id_categoria.nome]
                noticias_vistas[noticia_id] = noticia
                agrupadas.setdefault(tipo, {}).setdefault(veiculo, []).append(noticia)
            else:
                if v.id_categoria.nome not in noticias_vistas[noticia_id].categorias_cliente:
                    noticias_vistas[noticia_id].categorias_cliente.append(v.id_categoria.nome)

        context.update({
            "agrupadas": agrupadas,
            "cliente": cliente,
            "config": config,
        })
        return context
