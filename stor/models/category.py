from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    cate_name = models.CharField(max_length=20)

    def __str__(self):
        return self.cate_name