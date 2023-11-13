from django.contrib import admin
from Ecommerce_App.Article.models import Article
from Ecommerce_App.PostFiles.admin import Files_Article_Admin

# Third Party
from nested_admin import NestedModelAdmin


@admin.register(Article)
class Article_Admin(NestedModelAdmin):
    list_display = ['title', 'slug','uniqe_code', 'is_active', 'created_at']
    # filter_horizontal = ['categories']
    search_fields = ['title']
    date_hierarchy = 'created_at'
    inlines = [Files_Article_Admin,]
    exclude = ("slug",'uniqe_code')
