# Django
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

# Local
from Ecommerce_App.Product.models import Products
from Ecommerce_App.Commons.models import BaseModel

User = get_user_model()


class Comment(BaseModel):
    author = models.ForeignKey(
        User, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField(verbose_name=_("text"))
    product = models.ForeignKey(
        Products, related_name="comments", on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name=_("is active"), default=True)

    class Meta:
        db_table = "Comments"
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.text
