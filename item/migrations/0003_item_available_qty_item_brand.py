# Generated by Django 4.2.4 on 2023-08-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_rename_product_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='available_Qty',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='item',
            name='brand',
            field=models.CharField(default='', max_length=60),
        ),
    ]
