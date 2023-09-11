from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','avatar','slug','is_active','parent','created_at']
 