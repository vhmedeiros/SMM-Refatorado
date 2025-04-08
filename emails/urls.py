from django.urls import path
from . import views

app_name = "emails"

urlpatterns = [

    # 📬 Disparos de E-mail
    path("configuracoes/cliente/<int:id_cliente>/emails/", views.EmailDisparoListView.as_view(), name="email_list"),
    path("configuracoes/cliente/<int:id_cliente>/emails/novo/", views.EmailDisparoCreateView.as_view(), name="email_create"),
    path("configuracoes/cliente/<int:id_cliente>/emails/<int:pk>/editar/", views.EmailDisparoUpdateView.as_view(), name="email_update"),
    path("configuracoes/cliente/<int:id_cliente>/emails/<int:pk>/detalhes/", views.EmailDisparoDetailView.as_view(), name="email_detail"),
    path("configuracoes/cliente/<int:id_cliente>/emails/<int:pk>/toggle-status/", views.EmailDisparoToggleStatusView.as_view(), name="email_toggle_status"),

    # 👥 Destinatários Base (por cliente)
    path("configuracoes/cliente/<int:id_cliente>/destinatarios/", views.EmailDestinatarioBaseListView.as_view(), name="destinatario_base_list"),
    path("configuracoes/cliente/<int:id_cliente>/destinatarios/novo/", views.EmailDestinatarioBaseCreateView.as_view(), name="destinatario_base_create"),
    path("configuracoes/cliente/<int:id_cliente>/destinatarios/<int:pk>/editar/", views.EmailDestinatarioBaseUpdateView.as_view(), name="destinatario_base_update"),
    path("configuracoes/cliente/<int:id_cliente>/destinatarios/<int:pk>/excluir/", views.EmailDestinatarioBaseDeleteView.as_view(), name="destinatario_base_delete"),

    # 📥 Importação de CSV
    path("configuracoes/cliente/<int:id_cliente>/destinatarios/importar/", views.EmailDestinatarioBaseCSVImportView.as_view(), name="destinatario_base_csv_import"),
    path("configuracoes/cliente/<int:id_cliente>/destinatarios/modelo-csv/", views.baixar_modelo_destinatarios_csv, name="destinatario_base_modelo_csv"),

    # ROTAS HTMX para HORÁRIOS (ajustadas com id_cliente)
    path("configuracoes/cliente/<int:id_cliente>/email/<int:id_disparo>/horarios/gerenciar/", views.EmailHorarioDisparoManageView.as_view(), name="horario_manage"),
    path("htmx/cliente/<int:id_cliente>/email/<int:id_disparo>/horarios/listar/", views.htmx_list_horarios, name="htmx_list_horarios"),
    path("htmx/cliente/<int:id_cliente>/email/<int:id_disparo>/horarios/novo/", views.htmx_add_horario, name="htmx_add_horario"),
    path("htmx/cliente/<int:id_cliente>/email/horarios/<int:pk>/editar/", views.htmx_edit_horario, name="htmx_edit_horario"),
    path("htmx/cliente/<int:id_cliente>/email/horarios/<int:pk>/remover/", views.htmx_delete_horario, name="htmx_delete_horario"),

    # HTMX - Destinatários
    path("configuracoes/cliente/<int:id_cliente>/email/<int:id_disparo>/destinatarios/gerenciar/", views.EmailDestinatarioManageView.as_view(), name="destinatario_manage"),
    path("htmx/cliente/<int:id_cliente>/email/<int:id_disparo>/destinatarios/listar/", views.htmx_list_destinatarios, name="htmx_list_destinatarios"),
    path("htmx/cliente/<int:id_cliente>/email/<int:id_disparo>/destinatarios/novo/", views.htmx_add_destinatario, name="htmx_add_destinatario"),
    path("htmx/cliente/<int:id_cliente>/email/destinatarios/<int:pk>/editar/", views.htmx_edit_destinatario, name="htmx_edit_destinatario"),
    path("htmx/cliente/<int:id_cliente>/email/destinatarios/<int:pk>/remover/", views.htmx_delete_destinatario, name="htmx_delete_destinatario"),

    # HTMX – Grupos de destinatários
    path("htmx/cliente/<int:id_cliente>/email/<int:id_disparo>/destinatarios/grupo/", views.htmx_grupo_destinatarios, name="htmx_grupo_destinatarios"),
    path("htmx/cliente/<int:id_cliente>/email/<int:id_disparo>/destinatarios/grupo/importar/", views.htmx_importar_grupo_destinatarios, name="htmx_importar_grupo_destinatarios"),
    path("htmx/cliente/<int:id_cliente>/email/destinatarios/<int:pk>/toggle/", views.htmx_toggle_destinatario, name="htmx_toggle_destinatario"),

    # preview do disparo
    path("configuracoes/cliente/<int:id_cliente>/emails/<int:id_disparo>/preview/", views.preview_email_render, name="preview_email_render"),

    # 📧 Envio de E-mail
    path("configuracoes/cliente/<int:id_cliente>/email/<int:id_disparo>/enviar_manual/", views.enviar_email_manual, name="enviar_email_manual"),

]
