# Django
from django.contrib import admin

#Local
from .models import Address

#Third Party
from nested_admin import NestedStackedInline


class Address_admin(NestedStackedInline):
    model = Address
    list_display = ['user','created_at','updated_at']
    extra = 0
