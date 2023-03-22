from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from rest_framework.exceptions import ValidationError


class Employee(MPTTModel):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    email = models.EmailField()
    employment_date = models.DateField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')


    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
        max_level = 7
