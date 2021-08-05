from django.db import models

from main.models import Product


class Flat(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='flats')
    total_area = models.PositiveSmallIntegerField()