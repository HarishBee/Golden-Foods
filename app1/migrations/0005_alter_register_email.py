# Generated by Django 4.2.7 on 2024-01-10 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_forget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='Email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
