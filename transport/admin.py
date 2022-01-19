from django.contrib import admin

from .models import Car, Brand, Model, Color, BodyType, Truck, Agricultural, Special, Other_t

admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Color)
admin.site.register(BodyType)
admin.site.register(Truck)
admin.site.register(Agricultural)
admin.site.register(Special)
admin.site.register(Other_t)