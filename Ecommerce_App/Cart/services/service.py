# Local
from Ecommerce_App.Cart.models import Cart

# This function creates an instance of the cart class
def create_cart(*, user, product):
    return Cart.objects.create(user=user, product=product)

# This function delete an instance of the cart class
def delete_cart(*, user, product):
    return Cart.objects.filter(user=user, product=product).delete()

# Returns the final price for the shopping cart
def Calcute_Total_Price(user):
    carts = Cart.objects.filter(user=user)
    T_price = 0
    for cart in carts:
        if cart.product.has_discount:
            T_price += cart.product.price_dis
        else:
            T_price += cart.product.price
    return T_price
