# Generated by Django 5.1.6 on 2025-04-06 09:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_productrating_user_name_servicerating_user_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='services',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='services', to=settings.AUTH_USER_MODEL),
        ),
    ]
