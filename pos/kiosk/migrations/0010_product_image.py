# Generated by Django 5.0.6 on 2024-06-18 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiosk', '0009_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=' ', upload_to='products/'),
        ),
    ]