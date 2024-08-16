from rest_framework import serializers
from .models import Property, PropertyImage
import os
import random
from django.conf import settings

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image']

class PropertySerializer(serializers.ModelSerializer):
    
    # images = PropertyImageSerializer(many=True, read_only=True)
    images = serializers.SerializerMethodField(read_only=True)
    # username = serializers.CharField(source='owner.username')
    user_first_name = serializers.CharField(source='owner.first_name', read_only=True)
    user_last_name = serializers.CharField(source='owner.last_name', read_only=True)
    class Meta:
        model = Property
        fields = ['id', 'location', 'address', 'description', 'price', 'bedrooms', 'bathrooms', 
                  'balcony', 'area', 'home_type', 'images', 'user_first_name', 'user_last_name', 'latitude', 'longitude']
        read_only_fields = ['owner']

    def get_images(self, instance):
        if instance.owner.is_superuser:
            images_folder = os.path.join(settings.BASE_DIR, 'media/admin_uploads/Properties_images')
            return random.sample([{'image':('/media/admin_uploads/Properties_images/'+f)} for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))], random.randint(3,8))
        else:
            return PropertyImageSerializer(instance.images.all(), many=True).data

    def to_representation(self, instance):
        ret =  super().to_representation(instance)
        ret['images'] = self.get_images(instance)
        return ret