# Generated by Django 3.1.7 on 2021-11-30 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_product_location'),
        ('real_estate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='floor',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flat',
            name='rooms',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Vacation_home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_area', models.PositiveSmallIntegerField()),
                ('rooms', models.PositiveSmallIntegerField()),
                ('floor', models.PositiveSmallIntegerField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vacation_homes', to='main.product')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_area', models.PositiveSmallIntegerField()),
                ('rooms', models.PositiveSmallIntegerField()),
                ('floor', models.PositiveSmallIntegerField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sectors', to='main.product')),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_area', models.PositiveSmallIntegerField()),
                ('rooms', models.PositiveSmallIntegerField()),
                ('floor', models.PositiveSmallIntegerField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='real_estate', to='main.product')),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_area', models.PositiveSmallIntegerField()),
                ('rooms', models.PositiveSmallIntegerField()),
                ('floor', models.PositiveSmallIntegerField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='offices', to='main.product')),
            ],
        ),
    ]
