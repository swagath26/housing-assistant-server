from rest_framework import serializers
from .models import Property, PropertyImage
# import os
# import random
# from django.conf import settings

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['image']

# class Comment(object):
#     def __init__(self, image):
#         self.image = image

# class ImageSerializer(serializers.Serializer):
#     image = serializers.ImageField()

class PropertySerializer(serializers.ModelSerializer):
    # def get_images ():
    #     return random.sample([f for f in os.listdir(os.path.join(settings.BASE_DIR, 'main/data/Properties_images')) if os.path.isfile(os.path.join(os.path.join(settings.BASE_DIR, 'main/data/Properties_images'), f))], random.randint(3,8))

        
    # images = ImageSerializer(['1','2','3'], many=True)
    images = PropertyImageSerializer(many=True)
    # images = ImageSerializer(Comment(image='http://127.0.0.1:8000/media/property_images/property_111229/image3'))
    username = serializers.CharField(source='owner.username')
    user_first_name = serializers.CharField(source='owner.first_name')
    user_last_name = serializers.CharField(source='owner.last_name')
    class Meta:
        model = Property
        fields = '__all__'