# Generated by Django 3.0 on 2019-12-22 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20191221_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcategory',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]