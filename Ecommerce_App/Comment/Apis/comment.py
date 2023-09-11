from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from Ecommerce_App.Product.models import Products
from django.shortcuts import get_object_or_404
from Ecommerce_App.Comment.models import Comment
from Ecommerce_App.Comment.services.comment import create_comment

class CommentApi(APIView):

    class OutPutSerializer(serializers.ModelSerializer):
        #ای دی کاربر رو بر میگردونه بعد از ساخت کاربر این نکته رو درست کن
        class Meta:
            model = Comment
            fields = ("author", "text", "product", "created_at")

    class InPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ("text",)

    def get(self, request, Pslug):
        #This function returns the comments of a product.
        product = get_object_or_404(Products, slug=Pslug)
        comments = product.comments
        return Response(self.OutPutSerializer(comments, many=True, context={"request": request}).data, status=status.HTTP_200_OK)
        #return Response({"not found": "This product has no comments"}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request, Pslug):
        # در این قسمت باید احراز هویت حتما جک شود
        # In this section, you can check the comments and if there is no problem,
        # that comment can be registered
        
        serializer = self.InPutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = get_object_or_404(Products, slug=Pslug)
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
    
    def delete(self,request,Pslug):
        #در این قسمت باید احراز هویت حتما جک شود
        #This function causes the comment of that person to be deleted
        product = get_object_or_404(Products, slug=Pslug)
        product.comments.filter(author= request.user).delete()
        return Response({"delete":"ok , deleted"},status=status.HTTP_204_NO_CONTENT)
