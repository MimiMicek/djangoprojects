from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class LoginappConfig(AppConfig):
    name = 'loginapp'


class ProfilesConfig(AppConfig):
    name = 'loginapp'
    verbose_name = _('loginapp')

    def ready(self):
        import loginapp.signals