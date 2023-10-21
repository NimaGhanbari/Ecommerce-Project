from django.db import models
from Ecommerce_App.Commons.models import BaseModel
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from Ecommerce_App.Product.models import Products


User = get_user_model()


class Cart(BaseModel):
    user = models.ForeignKey(to=User, verbose_name=_(
        "user"), on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, verbose_name=_(
        "product"), on_delete=models.CASCADE)
    count = models.PositiveIntegerField(verbose_name=_("count"),default=1)
    # create time
    # update time
    
    class Meta:
        db_table = "Carts"
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")

    def __str__(self):
        return "محصول ذخیره شده در سبد کالا"
