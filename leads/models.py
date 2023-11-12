from django.db import models
from users.models import User
from companys.models import Company
# Create your models here.

class Leads(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=100, blank=False)
    message = models.CharField(max_length=1000, blank=False)
    age = models.IntegerField(blank=False)
    date_birthday = models.DateField(blank=False)
    newsletter = models.BooleanField(blank=False)
    auto_letter = models.BooleanField(blank=False)
    letter = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.ForeignKey(to=Company, on_delete=models.CASCADE, null=False)

    
    def __str__(self):
        return self.name
