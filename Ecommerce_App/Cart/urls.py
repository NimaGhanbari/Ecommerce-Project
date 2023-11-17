# Django
from django.contrib import admin
from django.urls import path, include,re_path

# Local
from Ecommerce_App.Cart.Apis.cartview import Cart_View , Total_Price


urlpatterns = [
    path('', Cart_View.as_view(), name='cart-add'),
    #path('<slug:product_slug>/', Cart_View.as_view(), name='cart-del'),
    path('total-price/',Total_Price.as_view(),name="Total_Price"),
    re_path(r'(?P<product_slug>[^/]+)/?',Cart_View.as_view(), name="cart-del"),
    
    
]
