# Generated by Django 4.2.6 on 2023-10-08 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0008_alter_groupeuser_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GroupeUser',
            new_name='groupe_user',
        ),
    ]