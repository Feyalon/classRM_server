# Generated by Django 4.2.6 on 2023-11-12 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0003_alter_company_options_company_description_and_more'),
        ('leads', '0002_leads_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='company_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='companys.company'),
            preserve_default=False,
        ),
    ]
