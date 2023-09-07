from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from Ecommerce_App.Category.models import Category
from Ecommerce_App.Product.models import Products
from django.shortcuts import get_object_or_404
from Ecommerce_App.Product.services.product_ser import Sort_By
from Ecommerce_App.Category.services.category_ser import is_subcategory
#from Ecommerce_App.Like.services.like import count_like,count_dislike,count_popular,count_reactions
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
        result = is_subcategory(categor)
        if result:
            return Response(self.CategorySerializer(result, context={"request":request}).data)
        else:
            products = Sort_By(Products.objects.filter(categories=categor))
            return Response(self.OutPutSerializer(products,many=True,context={"request":request}).data)
            
            
            
class PostDetailApi(APIView):
    
    class OutPutSerializer(serializers.ModelSerializer):
        categories = PostApi.CategorySerializer(many=True)
        class Meta:
            model = Products
            fields = ("title","description","price","slug","categories","is_enable","uniqe_code","count_reactions","created_at","updated_at")
    
    def get(self,request,Pslug):
        product = get_object_or_404(Products,slug=Pslug,is_enable=True)
        return Response(self.OutPutSerializer(product,context={"request":request}).data)
    
        
        