

from django.utils.text import slugify

from django.db.models.signals import pre_save
from django.dispatch import receiver
from Ecommerce_App.Product.models import Products



def generate_unique_slug(instance, new_slug=None):
    slug = None
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title, allow_unicode=True)
    qs = Products.objects.filter(slug=slug)
    if qs.exists():
        new_slug = f"{slug}-{qs.count()}"
        return generate_unique_slug(instance, new_slug=new_slug)
    return slug


@receiver(pre_save, sender=Products)
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = generate_unique_slug(instance)