# Generated by Django 4.2.6 on 2023-10-08 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupeUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.groupeuser'),
        ),
    ]
