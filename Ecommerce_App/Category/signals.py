# Django
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Local
from Ecommerce_App.Category.models import Category
from Ecommerce_App.Commons.Services.CommonService import generate_unique_slug


# This function listens to signals from Category which is of pre_save type,
# and when it receives such a signal, the function below is executed.
@receiver(pre_save, sender=Category)
def Category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = generate_unique_slug(instance,Category)
        