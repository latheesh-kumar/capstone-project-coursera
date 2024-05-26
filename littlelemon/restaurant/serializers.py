#define Serializer class for User model
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
 class Meta:
    model = User
    fields = ['url', 'username', 'email', 'groups']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name', 'price','description','inventory']
        depth = 1

class BookingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name','guest_number','comment']
        depth = 1