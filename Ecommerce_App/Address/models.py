from django.db import models
from Ecommerce_App.Commons.models import BaseModel
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.translation import ugettext_lazy as _


class Address(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    zipcode = models.IntegerField(verbose_name=_("zipcode"))
    
    class Meta:
        db_table = "Address"
        verbose_name = _("Address")
        verbose_name_plural = _("Address")