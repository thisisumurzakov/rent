# Generated by Django 3.1.7 on 2021-11-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211128_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
