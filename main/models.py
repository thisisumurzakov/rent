from django.db import models
from django.utils import timezone

from accounts.models import User
from taggit.managers import TaggableManager


class BaseCategory(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class City(BaseCategory):
    pass


class Category(BaseCategory):
    icon = models.ImageField(upload_to='category/', null=True, blank=True)


class Subcategory(BaseCategory):
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="child")
    icon = models.ImageField(upload_to='subcategory/', null=True, blank=True)


def upload_to(instance, filename):
    return f'posts/{filename}'


class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField()
    views = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=300)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=False)
    location = models.CharField(max_length=100, null=True, blank=True)
    favourite = models.ManyToManyField(User, related_name="fav_posts", blank=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related")
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Media(models.Model):
    media = models.FileField(upload_to='media/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='media')


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True, related_name="children"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"{self.user} - {self.product}"


class RatingStar(models.Model):
    value = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        ordering = ["-value"]


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.product}"


# class House():
#     """??????"""
#     TYPE = [
#         ('DO', '??????'),
#         ('FL', '??????????????'),
#         ('KO', '??????????????'),
#         ('CH', '?????????? ????????'),
#         ('DA', '????????'),
#         ('TA', '????????????????'),
#     ]
#
#     total_area = models.PositiveSmallIntegerField()
#     type_house = models.CharField(max_length=2, choices=TYPE)
#
#
# class Land():
#     """??????????"""
#     total_area = models.PositiveSmallIntegerField()
#
#
# class CommercialPremises():
#     """???????????????????????? ??????????????????"""
#     TYPE = [
#         ('MA', '????????????????/????????????'),
#         ('SA', '????????????'),
#         ('RE', '??????????????????/????????/????????'),
#         ('OF', '??????????'),
#         ('SK', '????????????'),
#         ('OT', '???????????????? ?????????????? ????????????'),
#         ('BA', '???????? ????????????'),
#         ('PP', '?????????????????? ?????????????????????????? ????????????????????'),
#         ('PS', '?????????????????? ???????????????????? ????????????????????'),
#         ('MA', '?????? (?????????? ?????????????????????????? ??????????)'),
#         ('CH', '?????????? ????????????'),
#         ('DR', '????????????'),
#     ]
#
#     total_area = models.PositiveSmallIntegerField()
#     type = models.CharField(max_length=2, choices=TYPE)


# class Motorcycle():
#     """????????????????"""
#     model = models.CharField(max_length=150)
#     year_issue = models.CharField(max_length=150)
#     engine_volume = models.PositiveSmallIntegerField()
#
#
# class OtherTransport():
#     """???????????? ??????????????????"""
#
#
# class Bus():
#     """??????????????"""
#     model = models.CharField(max_length=150)
#
#
# class FreightCar():
#     """???????????????? ????????????????????"""
#     model = models.CharField(max_length=150)
#     body_type = models.CharField(max_length=150)
#
#
# class SpecialEquipment():
#     """?????????????????????? ??????????????"""
#
#
# class AgriculturalMachinery():
#     """?????????????? ??????????????"""
#
#
# class WaterTransport():
#     """???????????? ??????????????????"""
#
#
# class EntertainmentTechnology():
#     """?????????????????????????????? ??????????????"""
#
#
# class BuildTechnology():
#     """?????????? ??????????????"""
#
#
# class Furniture():
#     """????????????"""
#
#
# class Dishes():
#     """????????????"""
#
#
# class AnotherHouseAndGarden():
#     """????????????"""
#
#
# class CountryHouse():
#
#     TYPE = [
#         ('DO', '??????'),
#         ('FL', '??????????????'),
#         ('KO', '??????????????'),
#         ('CH', '?????????? ????????'),
#         ('DA', '????????'),
#         ('TA', '????????????????'),
#     ]
#
#     name = models.CharField(max_length=150)
#     type_house = models.CharField(max_length=2, choices=TYPE)
#     number_rooms = models.PositiveSmallIntegerField()
#     internet = models.BooleanField(default=False)
#     air_conditioning = models.BooleanField(default=False)
#     refrigerator = models.BooleanField(default=False)
#     summer_pool = models.BooleanField(default=False)
#     winter_pool = models.BooleanField(default=False)
#     fireplace = models.BooleanField(default=False)
#     sauna = models.BooleanField(default=False)
#     table_tennis = models.BooleanField(default=False)
#     summer_kitchen = models.BooleanField(default=False)
#     brazier = models.BooleanField(default=False)
#     billiards = models.BooleanField(default=False)
#     tapchan = models.BooleanField(default=False)
#     toilet = models.BooleanField(default=False)
#     garage = models.BooleanField(default=False)
#     bathroom = models.BooleanField(default=False)
#     hot_water = models.BooleanField(default=False)
#     playground = models.BooleanField(default=False)
#     barbecue = models.BooleanField(default=False)
#     television = models.BooleanField(default=False)