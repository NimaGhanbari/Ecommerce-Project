# Django
from django.contrib.auth import get_user_model

User = get_user_model()


def Create_User(serialize, request):
    new_user = User.objects.create_user(phone_number=serialize.validated_data.get('phone_number'),
                                        password=serialize.validated_data.get('password'))
    return new_user
