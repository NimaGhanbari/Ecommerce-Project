# Django
from django.contrib import admin

# Third Party
from nested_admin import NestedStackedInline

# Local
from Ecommerce_App.PostFiles.models import Post_File

class Files_Admin(NestedStackedInline):
    model = Post_File
    fields = ['id','title','file_type','fil','is_active']
    extra = 0
    
