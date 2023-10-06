# Django
from django.contrib.auth import get_user_model

# REST Framework
from rest_framework.response import Response
from rest_framework import status

# Local
from Ecommerce_App.Like.models import Like
from Ecommerce_App.Product.models import Products

User = get_user_model()


def create_like(*, user: User, product: Products, value: str) -> Like | None:

    try:
        like = Like.objects.get(user=user, product=product)
        # for delete
        if like.value == value:
            like.delete()
            return None
        # for edit
        like.value = value
        like.save()
        return Response({"detail": "done successfully"}, status=status.HTTP_200_OK)
    except Like.DoesNotExist:
        # for create
        lik = Like.objects.create(
            user=user, product=product, value=value
        )
    return lik
