from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from Ecommerce_App.Product.models import Products
from django.shortcuts import get_object_or_404
from Ecommerce_App.Comment.models import Comment
#گت >>>  اسم محصول بگیرد یا اسلاگ و کامنت های اون محصول رو برگردوند
#پست  <<<<  کاربر میخواهد یک کامنت اضافه کند 

class CommentApi(APIView):
    
    class OutPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ("author","text","product","created_at")
    
    def get(self,request,Pslug):
        product = get_object_or_404(Products,slug=Pslug)
        comments = product.comments
        if len(comments) == 0:
            return Response({"not found":"This product has no comments"},status=status.HTTP_404_NOT_FOUND)
        return Response(self.OutPutSerializer(comments,many=True,context={"request":request}).data,status=status.HTTP_200_OK)
        
    
    
    def post(self,request,Pslug):
        pass


