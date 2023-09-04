from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from Ecommerce_App.Category.models import Category
from Ecommerce_App.Product.models import Products
from django.shortcuts import get_object_or_404
from Ecommerce_App.Product.services.product_ser import is_subcategory,Sort_By

class PostApi(APIView):
    
    
    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ('slug')
    
    class OutPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Products
            fields = ("title","price","slug","is_enable")
    
    
    def get(self,request,Cslug):
        categor = get_object_or_404(Category,slug=Cslug)
        result = is_subcategory(categor)
        if result:
            #اگر توش یه چیزی بود و زیر مجموعه داشت
            #تمام زیر مجموعه ها را بازم بر میگردونیم
            pass
        else:
            #تمام کالا های رو که با این دسته بندی هستند رو بر میگردونیم بر اساس ترتیب بندی شده
            products = Sort_By(Products.objects.filter(categories=categor))
            return Response(self.OutPutSerializer(products, context={"request":request}).data)
            
            
        