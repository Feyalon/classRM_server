from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    comment = models.CharField(max_length=250, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name