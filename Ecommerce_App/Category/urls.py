# Django
from django.urls import path, include

# Local
from .Apis.CategoryApis import Category_api

urlpatterns = [
    path("<int:types>/", Category_api.as_view(), name="category-list"),
    


]