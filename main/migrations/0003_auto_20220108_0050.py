# Generated by Django 3.1.7 on 2022-01-07 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211205_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
