from django.urls import path,include
from Ecommerce_App.Product.Apis.product import PostApi,PostDetailApi
from Ecommerce_App.Like.Apis.like import ReactionApi

urlpatterns = [
    path("<slug:Cslug>/list/",PostApi.as_view(),name="product-list"),
    path("<slug:Pslug>/detail/",PostDetailApi.as_view(),name="product-detail"),
    path("<slug:Pslug>/reaction/",include("Ecommerce_App.Like.urls")),
    path("<slug:Pslug>/comment/",include("Ecommerce_App.Comment.urls")),
    
        
]
