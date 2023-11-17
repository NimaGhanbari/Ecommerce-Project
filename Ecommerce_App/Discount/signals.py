# Django
from django.db.models.signals import pre_save,pre_delete
from django.dispatch import receiver

# Local
from Ecommerce_App.Discount.models import Discount
from Ecommerce_App.Product.models import Products

# -- The "receiver" function listens to the "discount" model of the "pre save" type and when receiving this signal,
# the "discount_pre_save_receiver" function is executed.
# -- When a instance of the "discount" model is produced, price changes are made on the instance before this instance is saved.
@receiver(pre_save, sender=Discount)
def discount_pre_save_receiver(sender, instance, *args, **kwargs):
    product = instance.product
    product.price_dis = product.price * ((100-instance.discount)/100)
    product.has_discount = True
    product.save()
    

# -- The "receiver" function listens to the "discount" model of the "pre delete" type and when receiving this signal,
# the "discount_pre_delete_receiver" function is executed.
# When an instance is removed from the discount model, this function causes the product price to change to the same initial value.
@receiver(pre_delete, sender=Discount)
def discount_pre_delete_receiver(sender, instance, *args, **kwargs):
    product = instance.product
    product.price_dis = 0
    product.has_discount = False
    product.save()

    