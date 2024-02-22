from django.core.management.base import BaseCommand
from main.models import Property
import googlemaps
    
class Command(BaseCommand):
    help = "Update the geocodes for property locations"
    
    def handle(self, *args, **option):
        def geocode(location):
            gmaps = googlemaps.Client(key='AIzaSyBo-ItKuuol693o7N6HX0VfzF1n3rvBmRo')
            geocode_result = gmaps.geocode(location)
            if geocode_result:
                geocode = geocode_result[0]['geometry']['location']
                return geocode['lat'], geocode['lng']
            else:
                return None, None
        for property_instance in Property.objects.all():
            address = property_instance.address + ',' + property_instance.location
            geo = geocode(address)
            property_instance.latitude = geo[0]
            property_instance.longitude = geo[1]
            property_instance.save()
        self.stdout.write(self.style.SUCCESS('Geocodes updated successfully..'))