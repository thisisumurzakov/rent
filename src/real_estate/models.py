from django.db import models

from main.models import Product


class Flat(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='flats')
    total_area = models.PositiveSmallIntegerField()
    rooms = models.PositiveSmallIntegerField()
    floor = models.PositiveSmallIntegerField()


class Office(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='offices')
    total_area = models.PositiveSmallIntegerField()
    rooms = models.PositiveSmallIntegerField()
    floor = models.PositiveSmallIntegerField()


class Sector(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='sectors')
    total_area = models.PositiveSmallIntegerField()
    rooms = models.PositiveSmallIntegerField()
    floor = models.PositiveSmallIntegerField()


class Vacation_home(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='vacation_homes')
    total_area = models.PositiveSmallIntegerField()
    rooms = models.PositiveSmallIntegerField()
    floor = models.PositiveSmallIntegerField()


class Other_r(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='real_estate')
    total_area = models.PositiveSmallIntegerField()
    rooms = models.PositiveSmallIntegerField()
    floor = models.PositiveSmallIntegerField()
