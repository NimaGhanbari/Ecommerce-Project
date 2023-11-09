from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',include("Ecommerce_App.Product.urls")),
    path('auth/',include("Ecommerce_App.Authentication.urls")),
    path('user/',include("Ecommerce_App.User.urls")),
    path('checkout/cart/',include("Ecommerce_App.Cart.urls")),
    path('checkout/shipping/',include("Ecommerce_App.Shipping.urls")),
    path('search/',include("Ecommerce_App.Search.urls")),
]
