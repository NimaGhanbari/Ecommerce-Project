from Ecommerce_App.Address.models import Address


def Create_Address(*, user, latitude, longitude, zipcode, Plaque) -> Address:
    address = Address.objects.create(
        user=user, latitude=latitude, longitude=longitude, zipcode=zipcode, Plaque=Plaque)
    return address