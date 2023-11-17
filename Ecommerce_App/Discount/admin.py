# Django
from django.contrib import admin

# Local
from .models import Discount

#Third Party
from nested_admin import NestedStackedInline


class Discount_admin(NestedStackedInline):
    model = Discount
    extra = 0