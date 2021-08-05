from django.contrib import admin

from .models import Car, Brand, Model, Color, BodyType

admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Color)
admin.site.register(BodyType)