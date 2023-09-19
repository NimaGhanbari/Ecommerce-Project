from Ecommerce_App.Address.models import Address


def Create_Address(*, user, latitude, longitude, zipcode, Plaque) -> Address:
    address = Address.objects.create(
        user=user, latitude=latitude, longitude=longitude, zipcode=zipcode, Plaque=Plaque)
    return address


def Update_Address(serialize, pk,request):
    new_Address = Address.objects.filter(id=pk,user=request.user).update(latitude=serialize.validated_data.get('latitude'),
                                                       longitude=serialize.validated_data.get(
                                                           'longitude'),
                                                       zipcode=serialize.validated_data.get(
                                                           'zipcode'),
                                                       Plaque=serialize.validated_data.get('Plaque'))
    return new_Address