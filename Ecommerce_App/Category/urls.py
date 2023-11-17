# Django
from django.urls import path, include

# Local
from .Apis.CategoryApis import Category_api

urlpatterns = [
    # PRODUCT = "1"
    # QUESTION = "2"
    # BRAND = "3"
    path("<int:types>/", Category_api.as_view(), name="category-list"),
    
]