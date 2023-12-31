# Django
from django.contrib import messages
from django.core.cache import cache
from django.contrib.auth import get_user_model

# Python
import random
import uuid
import json
from typing import Dict

# Third Party
from kavenegar import *

# REST Framework
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

# Local
from Ecommerce.settings_project import local_settings

User = get_user_model()


def SendSMS(phone: int, message: str) -> None | Exception:
    print(message)
    try:
        api = KavenegarAPI(local_settings.KAVENEGAR_KEY)
        params = {
            # Because we are in the development environment, there is no sender
            'sender': local_settings.SENDER,
            'receptor': f'{phone}',
            'message': f'{message}'
        }
        result = api.sms_send(params)
    except APIException as e:
        print(str(e))
        #باید خط پایین را از کامنت در بیاوریم و دو خط پایین را باید کامنت کنیم
        #return e
        return None
    except HTTPException as e:
        print(str(e))
        return e
    print(message)
    return None


def SendCode(phone: int) -> None | Exception:
    randcode = random.randint(10000, 99999)
    cache.set(str(phone), str(randcode), 3*60)
    message = f"""کد تایید:{randcode}
    شرکت تجارت الکترونیک """
    #خط پایین باید پاک شود
    print(message)
    return SendSMS(phone=phone, message=message)


def check(serialize) -> None:
    code = cache.get(str(serialize.validated_data.get("phone_number")))

    if serialize.validated_data.get("sms_code") != code:
        return Response({"detail": "The code sent is invalid"}, status=status.HTTP_400_BAD_REQUEST)
    if serialize.validated_data.get("password") != serialize.validated_data.get("confirm_password"):
        return Response({"detail": "The passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)
    return None


def get_object_email(email: str, password: str) -> None | User:
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    if not user.check_password(password):
        return None
    return user


def get_object_phone(phone_number: int, password: str) -> None | User:
    try:
        user = User.objects.get(phone_number=phone_number)
    except User.DoesNotExist:
        return None
    if not user.check_password(password):
        return None
    return user


def create_token(user: User) -> Dict[str,str]:
    refresh = RefreshToken.for_user(user)
    return {
        'access_token': str(refresh.access_token),
        'refresh_token': str(refresh)
    }
