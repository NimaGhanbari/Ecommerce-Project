# Django
from django.shortcuts import get_list_or_404
from django.http import JsonResponse

# REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Local
from Ecommerce_App.Address.models import Address
from Ecommerce_App.Address.services.address import Create_Address, Update_Address , Convert_Address

# Python
import json


class AddressApi(APIView):
    # *****The user must authenticate*****
    # In this class, there are APIs related to addresses, each function has its own activity
    # get    -> This function returns all user addresses
    # post   -> This function generates an address for the user in such a way that
    #          it takes latitude and longitude and a zipcode and license plate number and produces an address object.
    # put    -> This function replaces the received information with the previous information. (edits)
    # delete -> This function deletes the desired address
    # The post and put part can be written in the same way, but I used both sides

    permission_classes = [IsAuthenticated]
    
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Address
            fields = ('latitude', 'longitude', 'zipcode', 'Plaque')

    def get(self, request):
        Addresses = get_list_or_404(Address, user=request.user)
        text = Convert_Address(Addresses=Addresses)
        # When ensure_ascii is equal to false,
        # it means that the dumps function should convert non-English content such as Persian letters to json
        return Response(data=json.dumps(text, ensure_ascii=False), status=status.HTTP_200_OK)

    def post(self, request):
        serialize = self.OutputSerializer(data=request.data)
        if serialize.is_valid():
            try:
                new_address = Create_Address(user=request.user,
                                             latitude=serialize.validated_data.get(
                                                 "latitude"),
                                             longitude=serialize.validated_data.get(
                                                 "longitude"),
                                             zipcode=serialize.validated_data.get(
                                                 "zipcode"),
                                             Plaque=serialize.validated_data.get(
                                                 "Plaque")
                                             )
                return Response({"detail": "OK"}, status=status.HTTP_201_CREATED)
            except Exception as ex:
                return Response({"detail": f"ERROR: {ex}"})

        else:
            return Response({"detail": "not valid"})

    def delete(self, request, pk):
        try:
            Address.objects.get(id=pk, user=request.user).delete()
            return Response({"detail": "The address was successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
        except Address.DoesNotExist:
            return Response({"detail": "There is no address with this ID"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        serialize = self.OutputSerializer(data=request.data)
        if serialize.is_valid():
            try:
                New_Address = Update_Address(
                    serialize=serialize, pk=pk, request=request)
                return Response({"detail": "OK"}, status=status.HTTP_200_OK)
            except Exception as ex:
                return Response({"detail": f"ERROR: {ex}"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "not valid"},status=status.HTTP_400_BAD_REQUEST)
