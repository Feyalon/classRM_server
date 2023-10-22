from django.db import models
from users.models import User
# Create your models here.
class Company(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    website = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'companies'
        verbose_name = 'company'
        db_table = 'company'
        unique_together = ('user', 'name')
        indexes = [
            models.Index(fields=['user', 'name'], name='company_user_name_idx'),
        ]
        constraints = [
            models.UniqueConstraint(fields=('user', 'name'), name='company_user_name_uc'),
        ]
        default_permissions = ()
        permissions = (
            ('view_company', 'Can view company'),
            ('add_company', 'Can add company'),
            ('change_company', 'Can change company'),
            ('delete_company', 'Can delete company'),
        )