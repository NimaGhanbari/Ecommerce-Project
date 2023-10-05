# Django
from django.urls import path

# Local
from Ecommerce_App.Comment.Apis.comment import CommentApi

urlpatterns = [
    path('', CommentApi.as_view(), name="list-comment"),
]
