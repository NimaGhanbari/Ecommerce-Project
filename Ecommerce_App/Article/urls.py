# Django
from django.contrib import admin
from django.urls import path, include, re_path

# Local
from Ecommerce_App.Article.Apis.Article_Api import Article_view, Article_Detail_View

# In URL that use Persian expressions, we use re_path instead of path and we use regex.
urlpatterns = [
    path('<int:count>/', Article_view.as_view(), name='article-list'),
    # path('<slug:aslug>/', Article_Detail_View.as_view(), name='article-detail'),
    re_path(r'(?P<aslug>[^/]+)/?',
            Article_Detail_View.as_view(), name="article-detail"),
]
