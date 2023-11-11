

# Django
from django.contrib import admin
from django.urls import path, include

# Local
from Ecommerce_App.Article.Apis.Article_Api import Article_view


urlpatterns = [
    path('<int:count>/', Article_view.as_view(), name='article-list'),
]
