from django.contrib import admin

from .models import Flat, Office, Sector, Vacation_home, Other_r

admin.site.register(Flat)
admin.site.register(Office)
admin.site.register(Sector)
admin.site.register(Vacation_home)
admin.site.register(Other_r)