# Generated by Django 5.1.6 on 2025-04-08 18:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='product_images'),
        ),
        migrations.AlterField(
            model_name='services',
            name='service_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='service_images'),
        ),
    ]
