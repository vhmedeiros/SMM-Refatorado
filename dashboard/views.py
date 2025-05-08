# from django.views.generic import TemplateView
# from django.utils.timezone import localtime, now
# from django.contrib.auth.mixins import LoginRequiredMixin
# from noticias.models import NoticiaImportada
# from veiculos.models import TipoVeiculo
# from django.db.models import Count
# from datetime import timedelta, datetime

# class DashboardView(LoginRequiredMixin, TemplateView):
#     template_name = "dashboard/index.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # Agora com timezone local
#         agora = localtime(now())
#         hoje = agora.date()

#         # Faixas de tempo usando localtime
#         hora_atras = agora - timedelta(hours=1)
#         inicio_dia = agora.replace(hour=0, minute=0, second=0, microsecond=0)
#         fim_dia = agora.replace(hour=23, minute=59, second=59, microsecond=999999)
#         inicio_semana = hoje - timedelta(days=hoje.weekday())  # Segunda
#         inicio_mes = hoje.replace(day=1)
#         inicio_ano = hoje.replace(month=1, day=1)

#         # Contagem usando dt_importacao (campo de referência do sistema)
#         context["quantidades"] = {
#             "hora": NoticiaImportada.objects.filter(dt_importacao__gte=hora_atras).count(),
#             "dia": NoticiaImportada.objects.filter(dt_importacao__range=(inicio_dia, fim_dia)).count(),
#             "semana": NoticiaImportada.objects.filter(dt_importacao__date__gte=inicio_semana).count(),
#             "mes": NoticiaImportada.objects.filter(dt_importacao__date__gte=inicio_mes).count(),
#             "ano": NoticiaImportada.objects.filter(dt_importacao__date__gte=inicio_ano).count(),
#         }

#         # Origem das notícias
#         context["origem"] = {
#             "importadas": NoticiaImportada.objects.filter(id_importacao__isnull=False).count(),
#             "manuais": NoticiaImportada.objects.filter(id_importacao__isnull=True).count(),
#         }

#         # Tipos de veículo (tv, rádio, impresso, etc.)
#         context["tipos_veiculo"] = (
#             NoticiaImportada.objects
#             .values("cd_veiculo__tipo_veiculo__descricao_tipo_veiculo")
#             .annotate(total=Count("cd_noticia"))
#             .order_by("-total")
#         )

#         return context


from datetime import datetime, timedelta
from django.db.models.functions import TruncDate
from django.db.models import Count
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from noticias.models import NoticiaImportada
from veiculos.models import Veiculosistemas

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        hoje = datetime.today().date()
        inicio_semana = hoje - timedelta(days=hoje.weekday())
        inicio_mes = hoje.replace(day=1)
        inicio_ano = hoje.replace(month=1, day=1)

        # Contagens seguras sem timezone
        context["quantidades"] = {
            "hora": NoticiaImportada.objects.filter(dt_importacao__gte=datetime.now() - timedelta(hours=1)).count(),
            "dia": NoticiaImportada.objects.filter(dt_importacao__date=hoje).count(),
            "semana": NoticiaImportada.objects.filter(dt_importacao__date__gte=inicio_semana).count(),
            "mes": NoticiaImportada.objects.filter(dt_importacao__date__gte=inicio_mes).count(),
            "ano": NoticiaImportada.objects.filter(dt_importacao__date__gte=inicio_ano).count(),
        }

        # Origem
        context["origem"] = {
            "importadas": NoticiaImportada.objects.filter(id_importacao__isnull=False).count(),
            "manuais": NoticiaImportada.objects.filter(id_importacao__isnull=True).count(),
        }

        # Tipo de veículo
        context["tipos_veiculo"] = (
            NoticiaImportada.objects
            .values("cd_veiculo__tipo_veiculo__descricao_tipo_veiculo")
            .annotate(total=Count("cd_noticia"))
            .order_by("-total")
        )

        # Ranking dos veículos com mais notícias
        context["ranking_veiculos"] = (
            NoticiaImportada.objects
            .values("cd_veiculo__nome_veiculo")
            .annotate(total=Count("cd_noticia"))
            .order_by("-total")[:5]
        )

        return context
