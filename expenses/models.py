from django.db import models

# Create your models here.

class Budget(models.Model):
    quantity = models.IntegerField(blank=True)