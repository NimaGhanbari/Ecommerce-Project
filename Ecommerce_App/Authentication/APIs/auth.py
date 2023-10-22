# Django
from django.shortcuts import redirect
from django.core.cache import cache
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model

# REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

# Local
from Ecommerce_App.Authentication.services.service import SendCode, check, get_object_email, get_object_phone, create_token
from Ecommerce_App.User.services.create import Create_User


User = get_user_model()


class InitialAuth(APIView):

    class OutputSerializer(serializers.Serializer):
        phonemail = serializers.CharField()

    def get(self, request):
        return Response({"detail": "Please enter your phone number or email"})

    def post(self, request):
        serialize = self.OutputSerializer(data=request.data)
        if serialize.is_valid():
            phonemail = serialize.validated_data["phonemail"]
            if phonemail.isdigit():
                # if phonemail is number phone
                try:
                    User.objects.get(phone_number=phonemail)
                    print("1"*100)
                    return redirect(f"/auth/loginp/{phonemail}")
                except User.DoesNotExist:
                    result = SendCode(phone=phonemail)
                    if result != None:
                        messages.error(request, "Error")
                        return Response({"detail": f"ERROR: {result}"}, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        messages.success(
                            request, "The code has been sent to you")
                        return redirect("create_user")
            else:
                # if phonemail is email
                try:
                    User.objects.get(email=phonemail)
                    return redirect("login_email")
                except User.DoesNotExist:
                    messages.warning(
                        request, "There is no user with the entered email.If you want to enter the system for the first time, use the phone number.")
                    return redirect("initial")
        else:
            messages.error(request, "Error")
            return Response({"detail": "ERROR"}, status=status.HTTP_400_BAD_REQUEST)


class Create(APIView):
    # In this section, a page should be displayed where the user can send his information.
    # After sending, he should go to the post method to generate the user.
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
                messages.success(
                    request, "Your account has been successfully created")
                return redirect("initial")
                # return Response(status=status.HTTP_201_CREATED)
            except Exception as ex:
                return Response({"detail": f"ERROR: {ex}"})
        else:
            return Response({"detail": "data is not valid"}, status=status.HTTP_400_BAD_REQUEST)


class LoginEmail(APIView):
    # In this section, a page will be displayed to the user so that
    # the user can send his email and password so that the post method can send tokens to him.
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
            user = get_object_email(email=email, password=password)
            if user == None:
                return Response({"detail": "User with entered information not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response(create_token(user=user))

        else:
            return Response({"detail": "data is not valid"}, status=status.HTTP_400_BAD_REQUEST)


class LoginPhone(APIView):

    class OutputSerializer(serializers.Serializer):
        phone_number = serializers.CharField()
        password = serializers.CharField()

    def get(self, request, phonemail):
        return Response({"detail": f"Please send phone_number and password. phone:{phonemail}"})

    def post(self, request):
        print("post login p")
        serialize = self.OutputSerializer(data=request.data)
        if serialize.is_valid(raise_exception=True):
            phone = serialize.validated_data.get("phone_number")
            password = serialize.validated_data.get("password")
            user = get_object_phone(phone_number=phone, password=password)
            if user == None:
                return Response({"detail": "User with entered information not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response(create_token(user=user))
        else:
            return Response({"detail": "data is not valid"}, status=status.HTTP_400_BAD_REQUEST)
