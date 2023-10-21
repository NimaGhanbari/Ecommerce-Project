# Local
from .models import Cart

#Third Party
from nested_admin import NestedStackedInline

class Carts_admin(NestedStackedInline):
    model = Cart
    readonly_fields = ('user', 'product', 'count')
    extra = 0


