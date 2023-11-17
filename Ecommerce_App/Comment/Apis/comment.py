# Django
from django.shortcuts import get_object_or_404

# REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Local
from Ecommerce_App.Product.models import Products
from Ecommerce_App.Comment.models import Comment
from Ecommerce_App.Comment.services.comment import create_comment

class CommentApi(APIView):

    # get    -> This function returns the comments of a product.
    # post   -> In this section, authentication must be jacked
                # you can check the comments and if there is no problem, that comment can be registered
    # delete -> This function causes the comment of that person to be deleted
    class OutPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ("author", "text", "product", "created_at")

    class InPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ("text",)

    def get(self, request, Pslug):
        product = get_object_or_404(Products, slug=Pslug)
        comments = product.comments
        return Response(self.OutPutSerializer(comments, many=True, context={"request": request}).data, status=status.HTTP_200_OK)
    
    @permission_classes([IsAuthenticated])  
    def post(self, request, Pslug):
        serializer = self.InPutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = get_object_or_404(Products, slug=Pslug)
        # محتوای متنی پیام چک شود که مورد خاصی نداشته باشد
        try:
            Comment.objects.get(author=request.user,product= product)
            return Response({"detail":"You have already commented on this product"},status=status.HTTP_400_BAD_REQUEST)
        except Comment.DoesNotExist: 
            try:
                com = create_comment(
                    author=request.user,
                    text=serializer.validated_data.get("text"),
                    product=product
                )
            except Exception as ex:
                return Response(
                    {"detail": "Database Error - " + str(ex)},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response({"create": "Your comment has been successfully saved"}, status=status.HTTP_201_CREATED)
    
    @permission_classes([IsAuthenticated])
    def delete(self,request,Pslug):
        product = get_object_or_404(Products, slug=Pslug)
        product.comments.filter(author= request.user).delete()
        return Response({"delete":"ok , deleted"},status=status.HTTP_204_NO_CONTENT)
