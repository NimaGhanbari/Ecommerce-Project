# Django 
from django.contrib.auth import get_user_model

# Local
from Ecommerce_App.Comment.models import Comment
from Ecommerce_App.Product.models import Products


User = get_user_model()

# This function generates an instance of the comment model
def create_comment(*, author: User, text: str, product: Products) -> Comment:
    com = Comment.objects.create(
        author=author, text=text, product=product
    )
    return com