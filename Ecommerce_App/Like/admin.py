from django.contrib import admin
from Ecommerce_App.Like.models import Like
from nested_admin import NestedStackedInline


class Like_admin(NestedStackedInline):
    model = Like
    #list_display = ['author','text','product','is_active','created_at','updated_at']
    #date_hierarchy = 'created_at'
    extra = 0

