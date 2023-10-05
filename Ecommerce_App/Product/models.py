# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Local
from Ecommerce_App.Commons.models import BaseModel
from Ecommerce_App.Category.models import Category


class Products(BaseModel):
    title = models.CharField(_("title"), max_length=70)
    description = models.TextField(_("description"), blank=True)
    price = models.BigIntegerField(_("Price"))
    slug = models.SlugField(primary_key=True, max_length=100)
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
