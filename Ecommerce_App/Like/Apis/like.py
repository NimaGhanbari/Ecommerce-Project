# Django
from django.shortcuts import get_object_or_404

# Local
from Ecommerce_App.Like.models import Like
from Ecommerce_App.Product.models import Products
from Ecommerce_App.Like.services.like import create_like

# REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers


class ReactionApi(APIView):
    # In this section, authentication must be checked
    class InPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Like
            fields = ("value",)

    def put(self, request, Pslug):
        serializer = self.InPutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = get_object_or_404(Products, slug=Pslug)
        try:
            result = create_like(
                user=request.user, product=product, value=serializer.data["value"])
        except Exception as ex:
            return Response(
                {"detail": "Database Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(status=status.HTTP_201_CREATED)
