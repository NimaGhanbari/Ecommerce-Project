from django.db import models
from django.utils.translation import ugettext_lazy as _
from Ecommerce_App.Commons.models import BaseModel


class Products(BaseModel):
    title = models.CharField(_("title"), max_length=70)
    description = models.TextField(_("description"), blank=True)
    price = models.BigIntegerField(_("Price"))
    slug = models.SlugField(primary_key=True, max_length=100)
    # categories = models.ManyToManyField('Category',verbose_name=_("categories"))
    is_enable = models.BooleanField(_("is enable"), default=True)
    uniqe_code = models.PositiveIntegerField(
        verbose_name=_('uniqe_code'), unique=True)

    class Meta:
        db_table = "products"
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        return self.title
