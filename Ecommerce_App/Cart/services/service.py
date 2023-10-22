
from Ecommerce_App.Cart.models import Cart



def create_cart(*,user,product):
    return Cart.objects.create(user=user,product=product)

