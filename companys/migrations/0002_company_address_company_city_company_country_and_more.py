# Generated by Django 4.2.6 on 2023-10-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
    ]