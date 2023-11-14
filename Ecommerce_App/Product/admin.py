# Django
from django.contrib import admin

# Local
from Ecommerce_App.Comment.admin import Comments_admin
from Ecommerce_App.Like.admin import Like_admin
from Ecommerce_App.PostFiles.admin import Files_Admin
from Ecommerce_App.Category.models import Category
from Ecommerce_App.Discount.models import Discount
from .models import Products
from Ecommerce_App.Discount.admin import Discount_admin
# Third Party
from nested_admin import NestedModelAdmin


@admin.register(Products)
class Products_admin(NestedModelAdmin):
    list_display = ['title', 'price', 'slug','has_discount','Percent_Discount','price_dis',
                    'uniqe_code', 'is_enable', 'categor', 'created_at']

    def categor(self, obj):
        return ([category.title for category in obj.categories.all()])
    def Percent_Discount(self,obj):
        try:
            p = Discount.objects.get(product=obj)
            return p.discount
        except Discount.DoesNotExist:
            return 0
        
    filter_horizontal = ['categories']
    search_fields = ['title']
    date_hierarchy = 'created_at'
    inlines = [Comments_admin, Like_admin, Files_Admin,Discount_admin]
    exclude = ('slug','uniqe_code')
    readonly_fields = ('has_discount', 'price_dis')
