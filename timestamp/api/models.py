from django.db import models


# Create your models here.

class SimpleAPI(models.Model):
    unix = models.CharField(max_length=13)
    utc = models.DateTimeField()
