# Django
from django.contrib import admin

# Third Party
from nested_admin import NestedStackedInline

# Local
from Ecommerce_App.PostFiles.models import Post_File,Article_File

class Files_Admin(NestedStackedInline):
    model = Post_File
    #user add in fields
    fields = ['id','title','file_type','fil','is_active']
    extra = 0
    
    
class Files_Article_Admin(NestedStackedInline):
    model = Article_File
    fields = ['id','title','file_type','fil','is_active']
    extra = 0