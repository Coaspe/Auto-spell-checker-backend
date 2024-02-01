from django.apps import AppConfig
from dotenv import load_dotenv


class MainAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main_app"

    def ready(self) -> None:
        load_dotenv()
        return super().ready()
