from django.contrib import admin
from .models import Products

@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display = ['title','price','slug','uniqe_code','is_enable','created_at']
    search_fields = ['title']
