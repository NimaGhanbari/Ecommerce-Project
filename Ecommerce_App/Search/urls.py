# Django
from django.urls import path, include

# Local
from Ecommerce_App.Search.Apis.searchview import Search

urlpatterns = [
    path("", Search.as_view(), name="search-product"),
    

]