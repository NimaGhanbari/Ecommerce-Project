from django.urls import path
from Ecommerce_App.Product.Apis.product import PostApi,PostDetailApi
from Ecommerce_App.Like.Apis.like import ReactionApi

urlpatterns = [
    path("list/<slug:Cslug>/",PostApi.as_view(),name="product-list"),
    path("<slug:Pslug>/",PostDetailApi.as_view(),name="product-detail"),
    path("<slug:Pslug>/reaction/",ReactionApi.as_view(),name="product-reaction"),
    
        
]
