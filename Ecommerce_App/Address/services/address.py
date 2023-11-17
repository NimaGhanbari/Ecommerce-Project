# Local
from Ecommerce_App.Address.models import Address
from Ecommerce_App.User.models import BaseUser

# Third Party
from geopy.geocoders import Nominatim


# This function takes the address information and creates an address object
def Create_Address(*, user: BaseUser, latitude: float, longitude: float, zipcode: int, Plaque: int) -> Address:
    address = Address.objects.create(
        user=user, latitude=latitude, longitude=longitude, zipcode=zipcode, Plaque=Plaque)
    return address


# This function takes information about the new address and the pk and updates the address object
def Update_Address(serialize, pk: int, request) -> Address:
    new_Address = Address.objects.filter(id=pk, user=request.user).update(latitude=serialize.validated_data.get('latitude'),
                                                                          longitude=serialize.validated_data.get('longitude'),
                                                                          zipcode=serialize.validated_data.get('zipcode'),
                                                                          Plaque=serialize.validated_data.get('Plaque'))
    return new_Address


# This function takes a list of latitude and longitude and returns a list of addresses.
def Convert_Address(Addresses):
    geolocator = Nominatim(user_agent="Address")
    locations = []
    text = []
    for x in Addresses:
        locations.append(geolocator.reverse(
            f"{x.latitude}, {x.longitude}"))

    for x in locations:
        text.append(x.address)

    return text
