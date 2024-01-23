from django.db import models

class Property(models.Model):
    location = models.CharField(max_length=255)
    society = models.CharField(max_length=255)
    area_type = models.CharField(max_length=255)
    availability = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=255)
    bathrooms = models.IntegerField()
    balcony = models.IntegerField()
    area = models.CharField(max_length=255)
 
    def __str__(self):
        return self.price

def property_subfolder(instance, filename):
    property_id = instance.property.id
    return f'property_images/property_{property_id}/{filename}'

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='image_files', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=property_subfolder, blank=True, null=True)