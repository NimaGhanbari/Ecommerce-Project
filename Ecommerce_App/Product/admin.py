from django.contrib import admin
from .models import Products

@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display = ['title','price','slug','uniqe_code','is_enable','created_at']
    filter_horizontal = ['categories']
    search_fields = ['title']
    date_hierarchy = 'created_at'
