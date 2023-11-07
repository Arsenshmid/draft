from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' #позволяет задать тип поля, используемого по умолчанию для автоматически создаваемого первичного ключа в моделях
    name = 'myapp'

    def ready(self):
        import myapp.signals
