# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Local
from Ecommerce_App.Commons.models import BaseModel
from Ecommerce_App.Category.models import Category

from django.utils.text import slugify

from django.db.models.signals import pre_save
from django.dispatch import receiver

class Products(BaseModel):
    title = models.CharField(_("title"), max_length=70)
    description = models.TextField(_("description"), blank=True)
    price = models.BigIntegerField(_("Price"))
    slug = models.SlugField(primary_key=True, max_length=100, blank=True,allow_unicode=True)
    categories = models.ManyToManyField(Category, verbose_name=_("categories"))
    is_enable = models.BooleanField(_("is enable"), default=True)
    uniqe_code = models.PositiveIntegerField(
        verbose_name=_('uniqe_code'), unique=True)

    class Meta:
        db_table = "products"
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        return self.title

    @property
    def count_reactions(self):
        dict_count = {}
        dict_count["like"] = self.likes.filter(value="1").count()
        dict_count["dislike"] = self.likes.filter(value="2").count()
        dict_count["popular"] = self.likes.filter(value="3").count()
        return dict_count


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
