# Generated by Django 5.0.6 on 2024-06-18 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiosk', '0008_rename_order_id_payment_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=1),
        ),
    ]