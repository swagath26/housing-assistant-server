from rest_framework import serializers
from .models import Property, PropertyImage
from django.contrib.auth.models import User

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['image']

class PropertySerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True)
    username = serializers.CharField(source='owner.username')
    user_first_name = serializers.CharField(source='owner.first_name')
    user_last_name = serializers.CharField(source='owner.last_name')
    class Meta:
        model = Property
        fields = '__all__'