# Generated by Django 4.2.6 on 2023-10-22 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
