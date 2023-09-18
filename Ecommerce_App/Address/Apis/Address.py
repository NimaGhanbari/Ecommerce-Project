from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from Ecommerce_App.Address.models import Address
from django.shortcuts import get_list_or_404
from geopy.geocoders import Nominatim
from django.http import JsonResponse
import json


class AddressApi(APIView):
    #کاربر باید احراز هویت بکند
    def get(self,request):
        Addresses = get_list_or_404(Address,user=request.user)
        geolocator = Nominatim(user_agent="Address")
        locations = []
        text = []
        for x in Addresses:
            locations.append(geolocator.reverse(f"{x.latitude}, {x.longitude}"))
            
        for x in locations:
            text.append(x.address)
            
        return Response(data=json.dumps(text,ensure_ascii=False),status=status.HTTP_200_OK)
        

    
    def post(self,request):
        pass
    
    def delete(self,request):
        pass
    
    def put(self,request):
        pass

