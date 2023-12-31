# Django
from django.db.models import QuerySet

# Local
from Ecommerce_App.Category.models import Category

# This function returns the categories,if we give None input to it, the parent categories will be returned
def is_subcategory(categor: Category, type: str) -> QuerySet[Category] | None:
    return Category.objects.filter(parent=categor, is_active=True, type=type)
