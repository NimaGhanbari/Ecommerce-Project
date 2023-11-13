from django.db.models.signals import pre_save
from django.dispatch import receiver
from Ecommerce_App.Category.models import Category
from Ecommerce_App.Commons.Services.CommonService import generate_unique_slug



@receiver(pre_save, sender=Category)
def Category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = generate_unique_slug(instance,Category)
        