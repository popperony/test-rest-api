from django.apps import AppConfig


class PaletteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server.apps.palette'
    verbose_name = 'Палитры'

    def ready(self):
        from server.apps.palette import signals
