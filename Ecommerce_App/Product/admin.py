from django.contrib import admin
from .models import Products
from Ecommerce_App.Comment.admin import Comments_admin
from nested_admin import NestedModelAdmin
from Ecommerce_App.Category.models import Category

@admin.register(Products)
class Products_admin(NestedModelAdmin):
    list_display = ['title','price','slug','uniqe_code','is_enable','categor','created_at']
    def categor(self, obj):
        return ([Category.title for category in obj.categories.all()])
    filter_horizontal = ['categories']
    search_fields = ['title']
    date_hierarchy = 'created_at'
    inlines = [Comments_admin]
    
