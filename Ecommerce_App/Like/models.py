# Django
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Local
from Ecommerce_App.Product.models import Products
from Ecommerce_App.Commons.models import BaseModel


User = get_user_model()


class Like(BaseModel):

    LIKE = "1"
    DISLIKE = "2"
    POPULAR = "3"
    LIKE_CHOICES = (
        (LIKE, _('LIKE')),
        (DISLIKE, _('DISLIKE')),
        (POPULAR, _('POPULAR'))
    )

    # If the user is deleted, the like or delike remains
    user = models.ForeignKey(
        User, null=True, related_name="likes", on_delete=models.SET_NULL)
    product = models.ForeignKey(
        Products, related_name="likes", on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,
                             default='LIKE', max_length=15)
    # create time is inherited from BaseModel class
    # update time is inherited from BaseModel class

    def __str__(self):
        if self.value == "1":
            return "like"
        elif self.value == "2":
            return "dislike"
        elif self.value == "3":
            return "popular"
