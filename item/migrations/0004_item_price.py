# Generated by Django 4.2.4 on 2023-08-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item_available_qty_item_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=99),
        ),
    ]
