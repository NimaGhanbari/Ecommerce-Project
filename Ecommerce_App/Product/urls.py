# Django
from django.urls import path, include, re_path

# Local
from Ecommerce_App.Product.Apis.product import PostApi, PostDetailApi
from Ecommerce_App.Like.Apis.like import ReactionApi

urlpatterns = [
    # path("<slug:Cslug>/list/", PostApi.as_view(), name="product-list"),
    re_path("list/"r'(?P<Cslug>[^/]+)/?',
            PostApi.as_view(), name="product-list"),
    # path("<slug:Pslug>/detail/", PostDetailApi.as_view(), name="product-detail"),
    re_path("detail/"r'(?P<Pslug>[^/]+)/?',
            PostDetailApi.as_view(), name="product-detail"),
    # path("<slug:Pslug>/reaction/", include("Ecommerce_App.Like.urls")),
    re_path("reaction/"r'(?P<Pslug>[^/]+)/?',
            include("Ecommerce_App.Like.urls")),
    # path("<slug:Pslug>/comment/", include("Ecommerce_App.Comment.urls")),
    re_path("comment/"r'(?P<Pslug>[^/]+)/?',
            include("Ecommerce_App.Comment.urls")),


]
