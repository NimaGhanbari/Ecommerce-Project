from django.urls import path
from Ecommerce_App.Product.Apis.product import PostApi,PostDetailApi

urlpatterns = [
    path("list/<slug:Cslug>/",PostApi.as_view(),name="product-list"),
    path("<slug:Pslug>/",PostDetailApi.as_view(),name="product-detail"),
    
        
]
