from Ecommerce_App.Product.models import Products


def count_like(product):
    return product.likes.filter(value = "1").count()


def count_dislike(product):
    return product.likes.filter(value = "2").count()


def count_popular(product):
    return product.likes.filter(value = "3").count()

