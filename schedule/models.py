from django.db import models

# Create your models here.

class Schedule(models.Model):
    title = models.CharField(max_length=50, null=False)
    time = models.DateField(null=True, blank=True)
    room = models.IntegerField(null=False)
    group = models.CharField(max_length=10)
    def __str__(self):
        return str(self.title)