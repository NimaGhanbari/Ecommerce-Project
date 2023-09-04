from django.urls import path
from Ecommerce_App.Product.Apis.product import PostApi

urlpatterns = [
    path("list/<slug:Cslug>/",PostApi.as_view(),name="product-list"),
        
]
