# Django
from django.contrib import admin
from django.urls import path, include

# Local
from Ecommerce_App.Address.Apis.Address import AddressApi


urlpatterns = [
    path('', AddressApi.as_view(), name='address-list'),
    path('<int:pk>/', AddressApi.as_view(), name='address-detail'),
]
