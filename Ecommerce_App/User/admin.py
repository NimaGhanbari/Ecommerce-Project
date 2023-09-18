from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()
from Ecommerce_App.Address.admin import Address_admin
from nested_admin import NestedModelAdmin

class MyUserAdmin(UserAdmin,NestedModelAdmin):
    fieldsets = (
        (_('personal info'), {"fields": ('phone_number', 'password', 'name', 'email','nick_name','avatar','birthday','gender')}),
        (_('permissions'), {"fields": ('is_active', 'is_staff','is_superuser', 'user_permissions')}),
        (_('important dates'), {"fields": ('date_joined',)}),
    )

    add_fieldsets = [
        (None, {
            'classes': ('wide',),
            "fields": ('phone_number', 'password1', 'password2')
        })
    ]

    list_display = ('id', 'phone_number', 'email', 'is_staff')
    search_fields = ('phone_number__exact',)
    ordering = ('id',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    inlines = [Address_admin,]
    
    def email_view(self, obj):
        return obj.email
    email_view.empty_value_display = 'No known email'

    def phone_view(self, obj):
        return obj.phone_number
    phone_view.empty_value_display = 'No known phone'

    def get_search_results(self, request, queryset, search_term):
        queryset, may_have_duplicates = super().get_search_results(
            request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filter(
                phone_number=search_term_as_int)
        return queryset, may_have_duplicates


admin.site.unregister(Group)
admin.site.register(User, MyUserAdmin)
