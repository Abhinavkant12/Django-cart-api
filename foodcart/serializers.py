from rest_framework import serializers
from .models import CuisineType,Menu,MealType,State


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id','cuisine','name','description','price','menuImage','vegetarian','isActive')

class CuisineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuisineType
        fields = ('id','cuisine')

class MealTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealType
        fields = ('id','mealType')

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('id','state')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id','user','streetAddress','aptSuite','city','state','zipCode','phoneNumber','isActive')

        