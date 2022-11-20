from django.apps import AppConfig

class BracketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bracket'

    def ready(self):
        import bracket.signals
