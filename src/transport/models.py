from django.db import models

from main.models import Product, BaseCategory


class Brand(BaseCategory):
    pass


class Model(BaseCategory):
    pass


class BodyType(BaseCategory):
    pass


class Color(BaseCategory):
    pass


class Car(models.Model):
    FUEL_TYPE = (
        ('benzin', 'benzin'),
        ('elektr', 'elektr'),
        ('dizel', 'dizel')
    )

    TRANSMISSION = (
        ('mexanika', 'mexanika'),
        ('avtomat', 'avtomat')
    )
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='cars')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    body_type = models.ForeignKey(BodyType, on_delete=models.SET_NULL, null=True)
    fuel_type = models.CharField(max_length=6, choices=FUEL_TYPE)
    year_issue = models.PositiveSmallIntegerField()
    transmission = models.CharField(max_length=8, choices=TRANSMISSION)
    air_condition = models.BooleanField()
    position = models.CharField(max_length=1)
    mileage = models.IntegerField() #probeg


class Truck(models.Model):
    FUEL_TYPE = (
        ('benzin', 'benzin'),
        ('elektr', 'elektr'),
        ('dizel', 'dizel')
    )

    TRANSMISSION = (
        ('mexanika', 'mexanika'),
        ('avtomat', 'avtomat')
    )
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='trucks')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    body_type = models.ForeignKey(BodyType, on_delete=models.SET_NULL, null=True)
    fuel_type = models.CharField(max_length=6, choices=FUEL_TYPE)
    year_issue = models.PositiveSmallIntegerField()
    transmission = models.CharField(max_length=8, choices=TRANSMISSION)
    air_condition = models.BooleanField()
    position = models.CharField(max_length=1)
    mileage = models.IntegerField() #probeg


class Agricultural(models.Model):
    FUEL_TYPE = (
        ('benzin', 'benzin'),
        ('elektr', 'elektr'),
        ('dizel', 'dizel')
    )

    TRANSMISSION = (
        ('mexanika', 'mexanika'),
        ('avtomat', 'avtomat')
    )
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='agriculturals')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    body_type = models.ForeignKey(BodyType, on_delete=models.SET_NULL, null=True)
    fuel_type = models.CharField(max_length=6, choices=FUEL_TYPE)
    year_issue = models.PositiveSmallIntegerField()
    transmission = models.CharField(max_length=8, choices=TRANSMISSION)
    air_condition = models.BooleanField()
    position = models.CharField(max_length=1)
    mileage = models.IntegerField() #probeg


class Special(models.Model):
    FUEL_TYPE = (
        ('benzin', 'benzin'),
        ('elektr', 'elektr'),
        ('dizel', 'dizel')
    )

    TRANSMISSION = (
        ('mexanika', 'mexanika'),
        ('avtomat', 'avtomat')
    )
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='specials')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    body_type = models.ForeignKey(BodyType, on_delete=models.SET_NULL, null=True)
    fuel_type = models.CharField(max_length=6, choices=FUEL_TYPE)
    year_issue = models.PositiveSmallIntegerField()
    transmission = models.CharField(max_length=8, choices=TRANSMISSION)
    air_condition = models.BooleanField()
    position = models.CharField(max_length=1)
    mileage = models.IntegerField() #probeg


class Other_t(models.Model):
    FUEL_TYPE = (
        ('benzin', 'benzin'),
        ('elektr', 'elektr'),
        ('dizel', 'dizel')
    )

    TRANSMISSION = (
        ('mexanika', 'mexanika'),
        ('avtomat', 'avtomat')
    )
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='transport')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    body_type = models.ForeignKey(BodyType, on_delete=models.SET_NULL, null=True)
    fuel_type = models.CharField(max_length=6, choices=FUEL_TYPE)
    year_issue = models.PositiveSmallIntegerField()
    transmission = models.CharField(max_length=8, choices=TRANSMISSION)
    air_condition = models.BooleanField()
    position = models.CharField(max_length=1)
    mileage = models.IntegerField() #probeg