from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=250)
    owner_name = models.CharField(max_length=250)
    marked_for_deletion = models.BooleanField(default=False)
