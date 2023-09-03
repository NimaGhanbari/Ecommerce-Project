from django.db import models
from django.utils.translation import ugettext_lazy as _
from Ecommerce_App.Commons.models import BaseModel



class Category(BaseModel):
    title = models.CharField(verbose_name=_("title"),max_length=50)
    description = models.TextField(verbose_name=_("description"),blank=True)
    avatar = models.ImageField(verbose_name=_("avatar"),blank=True,upload_to='categories')
    is_active = models.BooleanField(verbose_name=_("is enable"),default=True)
    parent = models.ForeignKey('self',verbose_name=_("parent"),blank=True,null=True, on_delete= models.CASCADE)
    slug = models.SlugField(primary_key=True, max_length=100)
    code = models.PositiveIntegerField()
    class Meta:
        db_table = "categories"
        verbose_name = _("category")
        verbose_name_plural = _("categories")
        
    def __str__(self):
        return self.title