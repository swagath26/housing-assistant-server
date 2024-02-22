from django.core.management.base import BaseCommand
from main.models import Property, PropertyImage
import os
import random
from django.conf import settings
from django.core.files import File

class Command(BaseCommand):
    help = 'Load Property image data into the database'

    def handle(self, *args, **option):

        base_dir = settings.BASE_DIR
        images_folder = os.path.join(base_dir, 'main/data/Properties_images')
        image_files = [f for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))]

        for property_instance in Property.objects.all():
            selected_images = random.sample(image_files, random.randint(3,8))
            for i, image_file in enumerate(selected_images):
                image_path = os.path.join(images_folder, image_file)
                with open(image_path, 'rb') as f:
                    image = File(f, name=f"image{i}")
                    PropertyImage.objects.create(property = property_instance, image=image)

        self.stdout.write(self.style.SUCCESS('Images loaded successfully..'))