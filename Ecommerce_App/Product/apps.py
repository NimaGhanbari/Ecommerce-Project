from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Ecommerce_App.Product'
    
    def ready(self):
        import Ecommerce_App.Product.signals
