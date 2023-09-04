from django.urls import path
from Ecommerce_App.Comment.Apis.comment import CommentApi

urlpatterns = [
    path('<slug:Pslug>/',CommentApi.as_view(),name="list-comment"),
]