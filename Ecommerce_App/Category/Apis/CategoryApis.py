
# Django
from django.shortcuts import get_object_or_404

# REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

# local
from Ecommerce_App.Category.models import Category

class Category_api(APIView):
    
    class CategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ("title", "avatar", "slug")
    
    def get(self,request,types):
        return Response(self.CategorySerializer(Category.objects.filter(type=types,is_active=True),many=True,context={"request": request}).data)