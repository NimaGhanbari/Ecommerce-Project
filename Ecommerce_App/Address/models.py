# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

# Local
from Ecommerce_App.Commons.models import BaseModel

# Third Party
from geopy.geocoders import Nominatim


User = get_user_model()


class Address(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    zipcode = models.BigIntegerField(verbose_name=_("zipcode"))
    Plaque = models.PositiveIntegerField(
        verbose_name=_("Plaque"), blank=True, null=True)

    class Meta:
        db_table = "Address"
        verbose_name = _("Address")
        verbose_name_plural = _("Address")

    def __str__(self):
        geolocator = Nominatim(user_agent="Address")
        address = geolocator.reverse(f"{self.latitude}, {self.longitude}")
        return str(address.address)
