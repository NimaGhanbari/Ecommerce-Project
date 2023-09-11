from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True,auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
