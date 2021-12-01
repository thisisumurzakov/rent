# Generated by Django 3.1.7 on 2021-12-01 14:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_product_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='fav_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
