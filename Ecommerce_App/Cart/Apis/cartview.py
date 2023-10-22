# REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from django.contrib import messages
from django.shortcuts import redirect
from Ecommerce_App.Product.models import Products

from Ecommerce_App.Cart.services.service import create_cart
from rest_framework.permissions import IsAuthenticated


class Cart_View(APIView):

    # permission_classes = [IsAuthenticated]

    class OutPutSerializer(serializers.Serializer):
        product = serializers.CharField()

    def post(self, request):
        serialize = self.OutPutSerializer(data=request.data)
        if serialize.is_valid():
            product_slug = serialize.validated_data['product']
            product = None
            try:
                product = Products.objects.get(slug=product_slug)
            except Products.DoesNotExist():
                messages.error(request, "The desired product was not found")
                return redirect(request.META.get('HTTP_REFERER'))
            try:
                if Cart.objects.filter(user=user,product=product):
                    messages.warning(request,"قبلا تولید کردی برای افزایش تعداد کالا باید به سبد خرید مراجعه کنید")
                    return redirect(request.META.get('HTTP_REFERER'))
                create_cart(user=request.user, product=product)
                messages.success(
                    request, "The desired product has been added to the shopping cart")
            except Exception as e:
                messages.error(request, f"Database Error : {e}")
            # به خاطر اینکه ما با پستمن درخواست ارسال مسکنیم و از انجایی که ریدایرکت کرددیم آدرسی وجود ندارد و نان می باشد ارور می دهو
            # من فکر میکنم که اگر فرانت داشته باشد و در حالت واقعی از ریدایرکت کنیم ادرس قبلی دیگر نان نیست

        else:
            messages.error(
                request, "There was a problem adding the product to the shopping cart")
            
        return redirect(request.META.get('HTTP_REFERER'))
