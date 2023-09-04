from django.contrib import admin
from .models import Comment
from nested_admin import NestedStackedInline


class Comments_admin(NestedStackedInline):
    model = Comment
    list_display = ['author','text','product','is_active','created_at','updated_at']
    date_hierarchy = 'created_at'
    extra = 0


