from django.contrib import admin
from django.urls import path,include
from Ecommerce_App.Address.Apis.Address import AddressApi

urlpatterns = [
    path('', AddressApi.as_view(),name='get-address'),
]
