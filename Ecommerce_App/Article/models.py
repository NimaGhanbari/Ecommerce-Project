# Django
from django.db import models
from django_quill.fields import QuillField

# local
from Ecommerce_App.Commons.models import BaseModel

class Article(BaseModel):
    
    title = models.CharField(max_length=256,verbose_name="عنوان")
    # QuillField() : This field is for the admin to have access to an editor to prepare articles
    content = QuillField()
    slug = models.SlugField(primary_key=True, max_length=100,blank=True)
    is_active = models.BooleanField(default=True)
    uniqe_code = models.PositiveIntegerField(verbose_name="uniqe_code", unique=True)
    cover = models.ImageField(verbose_name="کاور مقاله", upload_to='Article/%Y/%m/%d/', blank=True, null=True)
    class Meta:
        db_table = "Articles"
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title

