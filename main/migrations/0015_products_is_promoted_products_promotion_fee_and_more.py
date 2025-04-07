# Generated by Django 5.1.6 on 2025-04-06 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_locationcategory_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_promoted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='products',
            name='promotion_fee',
            field=models.PositiveIntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='services',
            name='is_promoted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='services',
            name='promotion_fee',
            field=models.PositiveIntegerField(default=1000),
        ),
    ]
