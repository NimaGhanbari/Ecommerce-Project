from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from Ecommerce_App.Address.models import Address
from django.shortcuts import get_list_or_404
from geopy.geocoders import Nominatim
from django.http import JsonResponse
import json
from Ecommerce_App.Address.services.address import Create_Address


class AddressApi(APIView):
    #کاربر باید احراز هویت بکند
    
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Address
            fields = ('latitude','longitude','zipcode','Plaque')
    
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
        serialize = self.OutputSerializer(data=request.data)
        if serialize.is_valid():
            
            new_address = Create_Address(user=request.user,
                                         latitude=serialize.validated_data.get("latitude"),
                                         longitude=serialize.validated_data.get("longitude"),
                                         zipcode=serialize.validated_data.get("zipcode"),
                                         Plaque=serialize.validated_data.get("Plaque")
                                         )
            return Response({"detail":"OK"},status=status.HTTP_201_CREATED)
        else:
            return Response({"detail":"not valid"})
    
    def delete(self,request):
        pass
    
    def put(self,request):
        pass

