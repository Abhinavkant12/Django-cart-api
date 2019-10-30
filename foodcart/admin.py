from django.contrib import admin
from .models import CuisineType,Menu,Address,MenuRating,MealType,State
# Register your models here.

class ImageAdmin(admin.ModelAdmin):    
    readonly_fields = ('image_tag',)

admin.site.register(Menu, ImageAdmin)
admin.site.register(CuisineType)
admin.site.register(Address)
admin.site.register(MenuRating)
admin.site.register(MealType)
admin.site.register(State)