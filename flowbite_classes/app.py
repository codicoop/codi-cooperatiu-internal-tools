from django.apps import AppConfig


class FlowbiteClasses(AppConfig):
    name = "flowbite_classes"

    def ready(self):
        import flowbite_classes.monkey_patch  # noqa: F401
