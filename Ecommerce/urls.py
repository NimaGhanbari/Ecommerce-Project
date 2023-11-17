# Django
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

# Local
from Ecommerce.settings_project.local_settings import DEB

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',include("Ecommerce_App.Product.urls")),
    path('auth/',include("Ecommerce_App.Authentication.urls")),
    path('user/',include("Ecommerce_App.User.urls")),
    path('checkout/cart/',include("Ecommerce_App.Cart.urls")),
    path('search/',include("Ecommerce_App.Search.urls")),
    path('category/',include("Ecommerce_App.Category.urls")),
    path('article/',include("Ecommerce_App.Article.urls")),
]

# This part is for viewing static content and in production mode, this part should be removed.
if DEB:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)