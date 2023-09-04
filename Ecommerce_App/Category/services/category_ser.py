from Ecommerce_App.Category.models import Category


def Subcategory(categor):
    return Category.objects.filter(parent=categor,is_active=True)

def ParentCategory():
    return Category.objects.filter(parent=None,is_active=True)


