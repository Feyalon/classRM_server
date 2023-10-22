# Generated by Django 4.2.6 on 2023-10-08 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0007_alter_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupeuser',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]