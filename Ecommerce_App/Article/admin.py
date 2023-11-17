# Django
from django.contrib import admin

# Local
from Ecommerce_App.Article.models import Article

# Third Party
from nested_admin import NestedModelAdmin


@admin.register(Article)
class Article_Admin(NestedModelAdmin):
    list_display = ['title', 'slug','uniqe_code', 'is_active', 'created_at']
    search_fields = ['title']
    date_hierarchy = 'created_at'
    exclude = ("slug",'uniqe_code')
