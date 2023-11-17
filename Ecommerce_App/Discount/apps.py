from django.apps import AppConfig


class DiscountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Ecommerce_App.Discount'
    
    # To call the signal file
    def ready(self):
        import Ecommerce_App.Discount.signals