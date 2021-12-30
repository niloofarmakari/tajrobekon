from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ExperienceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.experience"
    verbose_name = _("Experience")
