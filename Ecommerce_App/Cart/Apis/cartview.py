# REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Django
from django.contrib import messages
from django.shortcuts import redirect

# Local
from Ecommerce_App.Product.models import Products
from Ecommerce_App.Cart.services.service import create_cart, delete_cart
from Ecommerce_App.Cart.models import Cart
from Ecommerce_App.Product.Apis.product import PostApi
from Ecommerce_App.Cart.services.service import Calcute_Total_Price

# Python
import json


class Cart_View(APIView):

    # permission_classes -> User must authenticate to access
    # get                -> This function returns the products in each user's shopping cart
    # post               -> This function creates a cart's object for the user, which automatically sets the counte value to 1
    # delete             -> A link should be shown to the user to remove the product from the shopping cart, which is referred to this function
    
    permission_classes = [IsAuthenticated]

    class InPutSerializer(serializers.Serializer):
        product = serializers.CharField()

    class OutPutSerializer(serializers.ModelSerializer):
        product = PostApi.OutPutSerializer()

        class Meta:
            model = Cart
            fields = ('id', 'product', 'created_at', 'updated_at')

    def get(self, request):
        return Response(self.OutPutSerializer(Cart.objects.filter(user=request.user), many=True, context={"request": request}).data)

    def post(self, request):
        # input: product -> اسلاگ محصول می باشد
        serialize = self.InPutSerializer(data=request.data)
        if serialize.is_valid():
            product_slug = serialize.validated_data['product']
            product = None
            try:
                product = Products.objects.get(slug=product_slug)
            except Products.DoesNotExist():
                messages.error(request, "The desired product was not found")
                return redirect(request.META.get('HTTP_REFERER'))
            try:
                if Cart.objects.filter(user=request.user, product=product):
                    messages.warning(
                        request, "قبلا تولید کردی برای افزایش تعداد کالا باید به سبد خرید مراجعه کنید")
                    return redirect(request.META.get('HTTP_REFERER'))
                create_cart(user=request.user, product=product)
                messages.success(
                    request, "The desired product has been added to the shopping cart")
            except Exception as e:
                messages.error(request, f"Database Error : {e}")

        else:
            messages.error(
                request, "There was a problem adding the product to the shopping cart")
        # به خاطر اینکه ما با پستمن درخواست ارسال میکنیم و از انجایی که ریدایرکت کرددیم آدرسی وجود ندارد و نان می باشد ارور می دهد
        # من فکر میکنم که اگر فرانت داشته باشد و در حالت واقعی از ریدایرکت کنیم ادرس قبلی دیگر نان نیست و دیگر این خطا را نداریم
        return redirect(request.META.get('HTTP_REFERER'))

    def delete(self, request, product_slug):
        # A link should be shown to the user to remove the product from the shopping cart, which is referred to this function
        product = None
        try:
            product = Products.objects.get(slug=product_slug)
        except Products.DoesNotExist():
            messages.error(request, "The desired product was not found")
            return redirect(request.META.get('HTTP_REFERER'))
        delete_cart(user=request.user, product=product)
        messages.success(
            request, "Das gewünschte Produkt wurde aus dem Warenkorb entfernt")
        # این در واقع همان خطایی هست که در متد پست داریم
        return redirect(request.META.get('HTTP_REFERER'))


class Total_Price(APIView):

    # permission_classes -> User must authenticate to access
    # get                -> Returns the final price for the shopping cart
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(data=json.dumps(Calcute_Total_Price(request.user)), status=status.HTTP_200_OK)
