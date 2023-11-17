# Django
from django.urls import path, include


urlpatterns = [
    path('addresses/', include("Ecommerce_App.Address.urls")),

]
