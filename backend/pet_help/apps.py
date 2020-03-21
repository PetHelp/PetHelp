from django.apps import AppConfig


class PetHelpConfig(AppConfig):
    name = "pet_help"

    def ready(self):
        import pet_help.signals
