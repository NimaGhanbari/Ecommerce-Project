# Django
from django.contrib import admin
from django.urls import path, include

# Local
from Ecommerce_App.Cart.Apis.cartview import Cart_View


urlpatterns = [
    path('', Cart_View.as_view(), name='cart-add'),
    #path('<slug:product_slug>/', Cart_View.as_view(), name='cart-del'),
    re_path(r'(?P<product_slug>[^/]+)/?',Cart_View.as_view(), name="cart-del"),
]
