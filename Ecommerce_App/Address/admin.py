from django.contrib import admin
from .models import Address
from nested_admin import NestedStackedInline


class Address_admin(NestedStackedInline):
    model = Address
    list_display = ['user','created_at','updated_at']
    extra = 0
