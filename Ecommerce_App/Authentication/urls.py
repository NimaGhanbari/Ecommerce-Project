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
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/', Create.as_view(), name='create_user'),
    path('logine/', LoginEmail.as_view(), name='login_email'),
    path('loginp/', LoginPhone.as_view(), name='login_phone'),
]
