from django.contrib import admin
from .models import Products

@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display = ['title','price','uniqe_code','is_enable']
    search_fields = ['title']
