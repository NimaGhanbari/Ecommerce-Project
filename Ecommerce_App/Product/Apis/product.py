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


class PostApi(APIView):

    class OutPutSerializer(serializers.ModelSerializer):
        files = FileSerializer(many=True)

        class Meta:
            model = Products
            fields = ("title", "price", "slug", "is_enable", "files")

    class CategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ("title", "avatar", "slug")

    def get(self, request, Cslug):
        """
        This function displays products without any filter or returns subcategories
        """
        categor = get_object_or_404(Category, slug=Cslug, is_active=True)
        result = is_subcategory(categor, "1")
        if result.count() != 0:
            return Response(self.CategorySerializer(result, many=True, context={"request": request}).data)
        else:
            products = Products.objects.filter(categories=categor)
            product_filter = Filtering(request, products)
            product_Order = Ordering(request, product_filter)
            return Response(self.OutPutSerializer(product_Order, many=True, context={"request": request}).data)


class PostDetailApi(APIView):

    class OutPutSerializer(serializers.ModelSerializer):
        categories = PostApi.CategorySerializer(many=True)
        files = FileSerializer(many=True)

        class Meta:
            model = Products
            fields = ("title", "description", "price", "slug", "categories", "is_enable",
                      "uniqe_code", "count_reactions", "files", "created_at", "updated_at")

    def get(self, request, Pslug):
        product = get_object_or_404(Products, slug=Pslug, is_enable=True)
        return Response(self.OutPutSerializer(product, context={"request": request}).data)
