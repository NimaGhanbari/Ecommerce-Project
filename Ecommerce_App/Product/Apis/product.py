from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from Ecommerce_App.Category.models import Category
from Ecommerce_App.Product.models import Products
from django.shortcuts import get_object_or_404
from Ecommerce_App.Product.services.product_ser import Sort_By
from Ecommerce_App.Category.services.category_ser import Subcategory

class PostApi(APIView):
    
    
    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ('slug')
    
    class OutPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Products
            fields = ("title","price","slug","is_enable")
    
    class CategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ("title","avatar","slug")
    
    def get(self,request,Cslug):
        """
        This function takes a slug and finds the category.
        If it has subcategories, it returns them, and if it doesn't,
        it returns the products based on the newest by default.
        """
        categor = get_object_or_404(Category,slug=Cslug,is_active=True)
        result = Subcategory(categor)
        if result:
            return Response(self.CategorySerializer(result, context={"request":request}).data)
        else:
            products = Sort_By(Products.objects.filter(categories=categor))
            return Response(self.OutPutSerializer(products, context={"request":request}).data)
            
            
        