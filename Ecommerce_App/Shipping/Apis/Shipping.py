# REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from Ecommerce_App.Address.models import Address
from Ecommerce_App.Address.services.address import Convert_Address


import json


class Shipping_view(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, tprice):
        # در این قسمت باید تمام آدرس های طرف و قیمت نهایی که با قیمت پست جمع شده را برگرداند
        # در این قسمت آدرس را که کاربر انتخاب کرده را به تابع پایین می فرستد
        print(request.user)
        print(type(request.user))
        addresess = Address.objects.filter(user=request.user)
        print(addresess)
        text = Convert_Address(addresess)
        tdict = {
            "totalprice": f"{tprice}",
            "text": f"{text}"
        }
        print(tdict)
        #  نباید به شکل زیر سریالایز شود و حتما باید سریالایزر نوشته شود
        return Response(data=json.dumps(tdict, ensure_ascii=False), status=status.HTTP_200_OK)

    def post(self, request):
        pass
