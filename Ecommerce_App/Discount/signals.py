from django.db.models.signals import pre_save,pre_delete
from django.dispatch import receiver
from Ecommerce_App.Discount.models import Discount
from Ecommerce_App.Product.models import Products

# هنگام تولید تخفیف قیمت محصول تغییر کند
@receiver(pre_save, sender=Discount)
def discount_pre_save_receiver(sender, instance, *args, **kwargs):
    product = instance.product
    product.price_dis = product.price * ((100-instance.discount)/100)
    product.has_discount = True
    product.save()
    
# قبل از حذف تخفیف قیمت محصول به قیمت قبلی برگردد
@receiver(pre_delete, sender=Discount)
def discount_pre_delete_receiver(sender, instance, *args, **kwargs):
    product = instance.product
    product.price_dis = 0
    product.has_discount = False
    product.save()

    