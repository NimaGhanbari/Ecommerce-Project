# Django
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Local
from Ecommerce_App.Product.models import Products
from Ecommerce_App.Commons.Services.CommonService import generate_unique_slug,generate_unique_code


# The receiver function receives the signals that return from the Products model, which is of the pre_save type.
# When receiving these types of signals, the following function is executed,
# which causes the slug and unique code to be set for each product before storage.
@receiver(pre_save, sender=Products)
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = generate_unique_slug(instance,Products)
        
    if not instance.uniqe_code:
        instance.uniqe_code = generate_unique_code(instance,Products)
        