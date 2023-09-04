from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class Comments_admin(admin.ModelAdmin):
    list_display = ['author','text','product','is_active','created_at','updated_at']
    date_hierarchy = 'created_at'


