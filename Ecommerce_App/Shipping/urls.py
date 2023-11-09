# Django
from django.contrib import admin
from django.urls import path, include

# Local
from Ecommerce_App.Shipping.Apis.Shipping import Shipping_view


urlpatterns = [
    path('<int:tprice>/', Shipping_view.as_view(), name='shipping-get'),
]
