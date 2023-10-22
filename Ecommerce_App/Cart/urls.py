# Django
from django.contrib import admin
from django.urls import path, include

# Local
from Ecommerce_App.Cart.Apis.cartview import Cart_View


urlpatterns = [
    path('', Cart_View.as_view(), name='cart-add'),
]
