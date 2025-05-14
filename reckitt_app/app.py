# reckitt_app/apps.py

from django.apps import AppConfig


class ReckittAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reckitt_app'
    verbose_name = 'ระบบจัดการผู้ใช้ LINE'

    def ready(self):
        # Import signal handlers
        import reckitt_app.signals