# Python 
import os
from pathlib import Path

from Ecommerce.settings_project import local_settings
from Ecommerce.settings_project.restframework_set import *


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = local_settings.SECRETKEY

DEBUG = local_settings.DEB

ALLOWED_HOSTS = local_settings.ALLOWEDHOSTS

LOCAL_APPS = [
    'Ecommerce_App.Product.apps.ProductConfig',
    'Ecommerce_App.Commons.apps.CommonsConfig',
    'Ecommerce_App.Category.apps.CategoryConfig',
    'Ecommerce_App.Comment.apps.CommentConfig',
    'Ecommerce_App.Like.apps.LikeConfig',
    'Ecommerce_App.PostFiles.apps.PostfilesConfig',
    'Ecommerce_App.User.apps.UserConfig',
    'Ecommerce_App.Authentication.apps.AuthenticationConfig',
    'Ecommerce_App.Address.apps.AddressConfig',
    
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'nested_admin',
    'django_filters',
    'rest_framework_simplejwt',
    
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Application definition

INSTALLED_APPS = [
    *LOCAL_APPS,
    *DJANGO_APPS,
    *THIRD_PARTY_APPS
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


#Because our program only responds to requests with the HTTP protocol, we use WSGA, otherwise we should have used ASGI.
WSGI_APPLICATION = 'Ecommerce.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': local_settings.NAME_DB, 
        'USER': local_settings.USER_DB,
        'PASSWORD': local_settings.PASSWORD_DB,
        'HOST': local_settings.HOST_DB, 
        'PORT': local_settings.PORT_DB,
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

AUTH_USER_MODEL = 'User.BaseUser'