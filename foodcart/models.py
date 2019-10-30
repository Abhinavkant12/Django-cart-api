import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.safestring import mark_safe

# Create your models here.


class MealType(models.Model):
    mealType = models.CharField(max_length=50)
    isActive = models.BooleanField(default=True)
    creation_date = models.DateTimeField('Creation Date',default=datetime.now())

    class Meta:
        db_table = 'mealTypes'

    def __str__(self):
        return self.mealType

class State(models.Model):
    state = models.CharField(max_length=50)
    isActive = models.BooleanField(default=True)
    creation_date = models.DateTimeField('Creation Date',default=datetime.now())

    class Meta:
        db_table = 'states'

    def __str__(self):
        return self.state


class CuisineType(models.Model):
    cuisine = models.CharField(max_length=50)
    isActive = models.BooleanField(default=True)
    creation_date = models.DateTimeField('Creation Date',default=datetime.now())

    class Meta:
        db_table = 'cuisineType'

    def __str__(self):
        return self.cuisine


class Menu(models.Model):
    cuisine        = models.ForeignKey(CuisineType, on_delete=models.CASCADE)
    name           = models.CharField(max_length=100)
    description    = models.TextField()
    price          = models.IntegerField(default=0)
    menuImage      = models.ImageField(upload_to='menu/') 
    vegetarian     = models.BooleanField(default=True)
    isActive       = models.BooleanField(default=True)
    creation_date  = models.DateTimeField('Creation Date',default=datetime.now())

    class Meta:
        db_table = 'menu'
    
    def url(self):
        return os.path.join('/',settings.MENU_URL, os.path.basename(str(self.menuImage)))

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="300" height="300" />'.format(self.url()) )
        image_tag.short_description = 'Image'  

    def __str__(self):
        return self.name

class Address(models.Model):
    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    streetAddress  = models.TextField('Street Address',default="")
    aptSuite       = models.TextField('Apt/Suite, Floor',default="")
    city           = models.CharField('City',max_length=100,default="")
    state          = models.ForeignKey(State, on_delete=models.CASCADE)
    zipCode        = models.CharField('Zip code',max_length=6,default="")
    phoneNumber    = models.CharField('Zip code',max_length=10,default="")
    creation_date  = models.DateTimeField('Creation Date',default=datetime.now())
    
    class Meta:
        db_table = 'address'

    def __str__(self):
        return self.user.address1

class MenuRating(models.Model):
    menu              = models.ForeignKey(Menu, on_delete=models.CASCADE)
    user              = models.ForeignKey(User, on_delete=models.CASCADE)  
    rating            = models.IntegerField(default=0)
    creation_date     = models.DateTimeField('Creation Date',default=datetime.now())

    class Meta:
        db_table = 'menu_ratings'

    # def __str__(self):
    #     return self.rating