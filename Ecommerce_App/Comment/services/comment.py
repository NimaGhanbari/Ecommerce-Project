from django.db.models import QuerySet
from Ecommerce_App.Comment.models import Comment


def create_comment(*, author, text, product) -> QuerySet[Comment]:
    com = Comment.objects.create(
        author=author, text=text, product=product
    )
    return com