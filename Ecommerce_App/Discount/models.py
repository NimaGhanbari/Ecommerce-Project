# Django
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Local
from Ecommerce_App.Product.models import Products
from Ecommerce_App.Commons.models import BaseModel


class Discount(BaseModel):
    # Because we don't have many objects of this model and the objects are deleted after the discount period ends,
    # there is no need to insert an index for search or filter.
    discount = models.IntegerField(verbose_name="درصد تخفیف", validators=[
                                   MinValueValidator(0), MaxValueValidator(100)])
    valid_from_discount = models.DateTimeField(
        verbose_name="شروع تخفیف")
    valid_end_discount = models.DateTimeField(
        verbose_name="پایان تخفیف")
    product = models.ForeignKey(
        Products, related_name="discounts", on_delete=models.CASCADE)

    class Meta:
        db_table = "Discounts"
        verbose_name = "Discount"
        verbose_name_plural = "Discounts"

    def __str__(self):
        return str(self.discount)
