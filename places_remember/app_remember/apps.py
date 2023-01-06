from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppRememberConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app_remember"
    verbose_name = _('места')
