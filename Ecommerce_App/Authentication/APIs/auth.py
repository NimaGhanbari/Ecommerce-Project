from Ecommerce_App.Authentication.services.service import SendCode, check, get_object_email, get_object_phone,create_token
from django.shortcuts import redirect
from django.core.cache import cache
from Ecommerce_App.User.services.create import Create_User
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib import messages
from django.contrib.auth import get_user_model


User = get_user_model()

class InitialAuth(APIView):

    class OutputSerializer(serializers.Serializer):
        phonemail = serializers.CharField()

    def get(self, request):
        return Response({"detail": "Please enter your phone number or email"})

    def post(self, request):
        serialize = self.OutputSerializer(data=request.data)
        phonemail = serialize.initial_data["phonemail"]
        if phonemail.isdigit():
            # if phonemail is number phone
            try:
                User.objects.get(phone_number=phonemail)
                return redirect("login_phone")
                #return Response({"detail":"already exist","url":"http://127.0.0.1:8000/auth/"})
            except User.DoesNotExist:
                result = SendCode(phone=phonemail)
                if result != None:
                    messages.error(request,"Error")
                    return Response({"detail": f"ERROR: {result}"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    messages.success(request,"The code has been sent to you")
                    return redirect("create_user")
        else:
            # if phonemail is email
            try:
                User.objects.get(email=phonemail)
                return redirect("login_email")
            except User.DoesNotExist:
                messages.warning(request,"There is no user with the entered email.If you want to enter the system for the first time, use the phone number.")
                return redirect("initial")


class Create(APIView):
    # در این قسمت باید یک صفحه ای نمایش داده شود که کاربر اطلاعات خودش رو ارسال کنه
    # بعد از ارسال باید به متد پست برود تا کاربر تولید شود

    class OutPutSerializer(serializers.Serializer):
        phone_number = serializers.CharField()
        password = serializers.CharField()
        confirm_password = serializers.CharField()
        sms_code = serializers.CharField()

    def get(self, request):
        return Response({"detail": "Please send the phone_number, sms_code, password and confirm_password"})

    def post(self, request):
        serialize = self.OutPutSerializer(data=request.data)
        if serialize.is_valid():
            check(serialize=serialize)
            try:
                new_user = Create_User(serialize=serialize, request=request)
                messages.success(request,"Your account has been successfully created")
                return redirect("initial")
                #return Response(status=status.HTTP_201_CREATED)
            except Exception as ex:
                return Response({"detail": f"ERROR: {ex}"})
        else:
            return Response({"detail": "data is not valid"}, status=status.HTTP_400_BAD_REQUEST)



class LoginEmail(APIView):
    # در این قسمت یک صفحه ای به کاربر نمایش داده میشود تا کاربر ایمیل و رمز خود را ارسال کند تا متد پست
    # برای اون توکن هایی ارسال کند

    class OutputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField()

    def get(self, request):
        return Response({"detail": "Please send email and password."})

    def post(self, request):
        serialize = self.OutputSerializer(data=request.data)
        if serialize.is_valid():

            email = serialize.validated_data.get("email")
            password = serialize.validated_data.get("password")
            user = get_object_email(email=email,password=password)
            if user == None:
                return Response({"detail": "User with entered information not found"}, status=status.HTTP_404_NOT_FOUND) 
            return Response(create_token(user=user))

        else:
            return Response({"detail": "data is not valid"}, status=status.HTTP_400_BAD_REQUEST)



class LoginPhone(APIView):

    class OutputSerializer(serializers.Serializer):
        phone_number = serializers.CharField()
        password = serializers.CharField()

    def get(self, request):
        return Response({"detail": "Please send phone_number and password."})

    def post(self, request):
        serialize = self.OutputSerializer(data=request.data)
        if serialize.is_valid(raise_exception=True):
            phone = serialize.validated_data.get("phone_number")
            password = serialize.validated_data.get("password")
            user = get_object_phone(phone_number=phone,password=password)
            if user == None:
                return Response({"detail": "User with entered information not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response(create_token(user=user))
        else:
            return Response({"detail": "data is not valid"}, status=status.HTTP_400_BAD_REQUEST)

