# Django
from django.urls import path

# Local
from Ecommerce_App.Like.Apis.like import ReactionApi

urlpatterns = [
    path('', ReactionApi.as_view(), name="reation-api"),
]
