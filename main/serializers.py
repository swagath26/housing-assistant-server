from rest_framework import serializers
from .models import Property, PropertyImage
import os
import random
from django.conf import settings

# class PropertyImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PropertyImage
#         fields = ['image']

class PropertySerializer(serializers.ModelSerializer):
    
    # images = PropertyImageSerializer(many=True)
    images = serializers.SerializerMethodField()
    username = serializers.CharField(source='owner.username')
    user_first_name = serializers.CharField(source='owner.first_name')
    user_last_name = serializers.CharField(source='owner.last_name')
    class Meta:
        model = Property
        fields = '__all__'

    def get_images(self, instance):
        images_folder = os.path.join(settings.BASE_DIR, 'media/admin_uploads/Properties_images')
        return random.sample([{'image':('/media/admin_uploads/Properties_images/'+f)} for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))], random.randint(3,8))

    def to_representation(self, instance):
        ret =  super().to_representation(instance)
        ret['images'] = self.get_images(instance)
        return ret