

from django.utils.text import slugify

from django.db.models.signals import pre_save
from django.dispatch import receiver
from Ecommerce_App.Article.models import Article
from Ecommerce_App.Commons.Services.CommonService import generate_unique_slug

@receiver(pre_save, sender=Article)
def Set_Slug_for_Article(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug =generate_unique_slug(instance,Article)
    