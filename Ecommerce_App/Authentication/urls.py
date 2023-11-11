# Django
from django.urls import path, include

# REST Framework
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Local
from Ecommerce_App.Authentication.APIs.auth import InitialAuth, Create, LoginEmail, LoginPhone

urlpatterns = [
    path('init/', InitialAuth.as_view(), name='initial'),
    # path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/<str:phone>/', Create.as_view(), name='create_user'),
    path('create/', Create.as_view(), name='create_user_2'),
    path('logine/<str:email>/', LoginEmail.as_view(), name='login_email'),
    path('logine/', LoginEmail.as_view(), name='login_email_2'),
    path('loginp/<str:phone>/', LoginPhone.as_view(), name='login_phone'),
    path('loginp/', LoginPhone.as_view(), name='login_phone_2'),
]
