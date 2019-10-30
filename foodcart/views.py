from django.shortcuts import render
from rest_framework import viewsets,permissions
from .permissions import IsOwnerOrReadOnly
from .models import CuisineType,Menu,MealType,Address,State
from .serializers import CuisineTypeSerializer,MenuSerializer,MealTypeSerializer,AddressSerializer,StateSerializer

class MenuViewSet(viewsets.ModelViewSet):
        queryset         = Menu.objects.all()
        serializer_class = MenuSerializer
        permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class CuisineViewSet(viewsets.ModelViewSet):
        queryset   = CuisineType.objects.all()
        serializer_class = CuisineTypeSerializer
        permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]       

class MealTypeViewSet(viewsets.ModelViewSet):
        queryset   = MealType.objects.all()
        serializer_class = MealTypeSerializer
        permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class AddressViewSet(viewsets.ModelViewSet):
        queryset   = Address.objects.all()
        serializer_class = AddressSerializer

class StateViewSet(viewsets.ModelViewSet):
        queryset   = State.objects.all()
        serializer_class = StateSerializer
        permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
        