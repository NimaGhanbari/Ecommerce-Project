# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from Ecommerce_App.Product.models import Products
from Ecommerce_App.Article.models import Article
from Ecommerce_App.Commons.models import BaseModel


class Post_File(BaseModel):
    FILE_VIDEO = 1
    FILE_IMG = 2
    FILE_TYPES = (
        (FILE_VIDEO, _('video')),
        (FILE_IMG, _('image'))
    )
    title = models.CharField(_("title"), max_length=50)
    file_type = models.PositiveSmallIntegerField(
        _("file type"), choices=FILE_TYPES)
    fil = models.FileField(_("file"), upload_to="products/%Y/%m/%d/")
    product = models.ForeignKey(Products, verbose_name=_(
        "Product"), related_name='files', on_delete=models.CASCADE)
    is_active = models.BooleanField(_("is enable"), default=True)

    class Meta:
        db_table = "files"
        verbose_name = _("file")
        verbose_name_plural = _("files")

    def __str__(self):
        return self.title


class Article_File(BaseModel):
    FILE_VIDEO = 1
    FILE_IMG = 2
    FILE_PDF = 3
    FILE_TYPES = (
        (FILE_VIDEO, "ویدیو"),
        (FILE_IMG, "تصویر"),
        (FILE_PDF, "PDF")
    )
    title = models.CharField("عنوان", max_length=50)
    file_type = models.PositiveSmallIntegerField(choices=FILE_TYPES)
    fil = models.FileField(_("فایل"), upload_to="Article/%Y/%m/%d/")
    articel = models.ForeignKey(Article, verbose_name="مقاله", related_name='files', on_delete=models.CASCADE)
    is_active = models.BooleanField("فعال", default=True)

    class Meta:
        db_table = "Article_files"
        verbose_name = _("Article_file")
        verbose_name_plural = _("Article_files")

    def __str__(self):
        return self.title