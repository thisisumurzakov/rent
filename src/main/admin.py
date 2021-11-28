from django.contrib import admin

from .models import Category, Subcategory, City, Product, Rating, RatingStar, Review, Media

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

class CategoryChildAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, CategoryChildAdmin)
admin.site.register(City)
admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Review)
admin.site.register(Media)