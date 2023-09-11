from django.contrib import admin
from nested_admin import NestedStackedInline
from Ecommerce_App.PostFiles.models import Post_File

class Files_Admin(NestedStackedInline):
    model = Post_File
    #user add in fields
    fields = ['id','title','file_type','fil','is_active']
    extra = 0