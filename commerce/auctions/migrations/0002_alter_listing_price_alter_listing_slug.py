# Generated by Django 4.2.2 on 2023-06-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.FloatField(verbose_name='Starting bid'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='slug',
            field=models.SlugField(max_length=400, unique=True, verbose_name='URL part (slug)'),
        ),
    ]