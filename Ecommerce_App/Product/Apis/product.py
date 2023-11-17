# Django
from django.shortcuts import get_object_or_404

# REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

# Local
from Ecommerce_App.Category.models import Category
from Ecommerce_App.Product.models import Products
from Ecommerce_App.Product.services.product_ser import Sort_By, FileSerializer, Filtering, Ordering
from Ecommerce_App.Category.services.category_ser import is_subcategory
from Ecommerce_App.PostFiles.models import Post_File
from Ecommerce_App.Category.Apis.CategoryApis import Category_api

class PostApi(APIView):
    # get -> This function returns products by category.
    # In this part, it first takes a slug from the category and checks whether that category has subcategories or not.
    # If it has subcategories, it returns subcategories,
    # but if not, it will filter and sort based on the fields and returns the information in the form of Json
    class OutPutSerializer(serializers.ModelSerializer):
        files = FileSerializer(many=True)

        class Meta:
            model = Products
            fields = ("title", "price", "slug", "is_enable", "files")

    

    def get(self, request, Cslug):
        categor = get_object_or_404(Category, slug=Cslug, is_active=True)
        result = is_subcategory(categor, "1")
        if result.count() != 0:
            return Response(Category_api.CategorySerializer(result, many=True, context={"request": request}).data)
        else:
            products = Products.objects.filter(categories=categor)
            product_filter = Filtering(request, products)
            product_Order = Ordering(request, product_filter)
            return Response(self.OutPutSerializer(product_Order, many=True, context={"request": request}).data)


class PostDetailApi(APIView):

    # get -> In this function, the details of each product are returned.
    
    class OutPutSerializer(serializers.ModelSerializer):
        categories = Category_api.CategorySerializer(many=True)
        files = FileSerializer(many=True)

        class Meta:
            model = Products
            fields = ("title", "description", "price", "slug", "categories", "is_enable",
                      "uniqe_code", "count_reactions", "files", "created_at", "updated_at")

    def get(self, request, Pslug):
        product = get_object_or_404(Products, slug=Pslug, is_enable=True)
        return Response(self.OutPutSerializer(product, context={"request": request}).data)
