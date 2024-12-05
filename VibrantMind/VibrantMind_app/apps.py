from django.apps import AppConfig


class VibrantmindAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'VibrantMind_app'

    def ready(self):
        import VibrantMind_app.signals