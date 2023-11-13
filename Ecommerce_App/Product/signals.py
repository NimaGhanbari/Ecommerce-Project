from django.db.models.signals import pre_save
from django.dispatch import receiver
from Ecommerce_App.Product.models import Products
from Ecommerce_App.Commons.Services.CommonService import generate_unique_slug,generate_unique_unique_code



@receiver(pre_save, sender=Products)
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = generate_unique_slug(instance,Products)
        
    if not instance.uniqe_code:
        instance.uniqe_code = generate_unique_unique_code(instance,Products)
        