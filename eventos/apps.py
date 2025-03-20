from django.apps import AppConfig


class EventosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "eventos"

    def ready(self):
        import eventos.signals  # 🔥 Importa os signals automaticamente ao iniciar o Django