from Ecommerce_App.Category.models import Category


def is_subcategory(categor):
    """
    This function returns the categories,
    if we give None input to it, the parent categories will be returned
    """
    return Category.objects.filter(parent=categor,is_active=True)


