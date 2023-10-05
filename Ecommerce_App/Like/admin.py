# django
from django.contrib import admin

# Local
from Ecommerce_App.Like.models import Like

#Third Party
from nested_admin import NestedStackedInline


class Like_admin(NestedStackedInline):
    model = Like
    extra = 0

