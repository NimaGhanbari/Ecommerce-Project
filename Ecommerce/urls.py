from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',include("Ecommerce_App.Product.urls")),
    path('auth/',include("Ecommerce_App.Authentication.urls")),
]
