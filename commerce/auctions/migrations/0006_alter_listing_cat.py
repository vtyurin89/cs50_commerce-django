# Generated by Django 4.2.2 on 2023-06-21 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_bid_bid_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.category', verbose_name='Category'),
        ),
    ]