

# REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from Ecommerce_App.Product.models import Products

from Ecommerce_App.Product.services.product_ser import Filtering
from Ecommerce_App.Product.Apis.product import PostApi

class Search(APIView):
    
    
    def get(self,request):
        title = request.GET.get('title')
        products = Products.objects.filter(title__icontains = title)
        return Response(PostApi.OutPutSerializer(products, many=True, context={"request": request}).data)
    