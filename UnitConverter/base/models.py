

# Create your models here.
# converter/models.py
from django.db import models

class Conversion(models.Model):
    from_unit = models.CharField(max_length=20)
    to_unit = models.CharField(max_length=20)
    value = models.FloatField()
    converted_value = models.FloatField()
