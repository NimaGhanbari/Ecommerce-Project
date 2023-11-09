# REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from django.contrib import messages
from django.shortcuts import redirect
from Ecommerce_App.Product.models import Products

from Ecommerce_App.Cart.services.service import create_cart, delete_cart
from rest_framework.permissions import IsAuthenticated
from Ecommerce_App.Cart.models import Cart
from Ecommerce_App.Product.Apis.product import PostApi


class Cart_View(APIView):

    permission_classes = [IsAuthenticated]

    class InPutSerializer(serializers.Serializer):
        product = serializers.CharField()

    class OutPutSerializer(serializers.ModelSerializer):
        product = PostApi.OutPutSerializer()

        class Meta:
            model = Cart
            fields = ('id', 'product', 'created_at', 'updated_at')

    def get(self, request):
        # باید قیمت نهایی هم ارسال شود
        carts = Cart.objects.filter(user=request.user)
        return Response(self.OutPutSerializer(carts, many=True, context={"request": request}).data)

    def post(self, request):
        #  زمانی که کاربر میخواهد این محصول را به سبد خرید اضافه کند به این تابع ارجاع داده میشود
        # Address: cart/
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
                if Cart.objects.filter(user=user, product=product):
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
        # به خاطر اینکه ما با پستمن درخواست ارسال مسکنیم و از انجایی که ریدایرکت کرددیم آدرسی وجود ندارد و نان می باشد ارور می دهو
        # من فکر میکنم که اگر فرانت داشته باشد و در حالت واقعی از ریدایرکت کنیم ادرس قبلی دیگر نان نیست
        return redirect(request.META.get('HTTP_REFERER'))

    def delete(self, request, product_slug):
        # باید یک لینکی به کاربر نشان داده شود که کالا را از سبد خرید حذف کند که به این تابع ارجاع داده میشود
        # Address: cart/<str:product_slug>/
        # input : product_slug -> اسلاگ محصول
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
