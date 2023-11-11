from django.db import models
from Ecommerce_App.Commons.models import BaseModel
from ckeditor.fields import RichTextField


class Article(BaseModel):
    
    title = models.CharField(max_length=128,verbose_name="عنوان")
    content = RichTextField()
    slug = models.SlugField(primary_key=True, max_length=100)
    is_active = models.BooleanField(default=True)
    uniqe_code = models.PositiveIntegerField(verbose_name="uniqe_code", unique=True)
    class Meta:
        db_table = "Articles"
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title

