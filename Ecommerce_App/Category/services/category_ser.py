from Ecommerce_App.Category.models import Category


def is_subcategory(categor):
    return Category.objects.filter(parent=categor,is_active=True)


