# Generated by Django 4.2.6 on 2023-10-21 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
                ('age', models.IntegerField()),
                ('date_birthday', models.DateField()),
                ('newsletter', models.BooleanField()),
                ('auto_letter', models.BooleanField()),
                ('letter', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
