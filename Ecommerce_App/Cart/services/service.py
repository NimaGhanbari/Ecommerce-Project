
from Ecommerce_App.Cart.models import Cart

from django.db.models import F


def create_cart(*, user, product):
    return Cart.objects.create(user=user, product=product)


def delete_cart(*, user, product):
    return Cart.objects.filter(user=user, product=product).delete()
