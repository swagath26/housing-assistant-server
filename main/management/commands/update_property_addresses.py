from django.core.management.base import BaseCommand
from main.models import Property
import random
# import requests

class Command(BaseCommand):
    help = "Update addresses and locations for property"
    
    def handle(self, *args, **option):

        # def get_nearby_places(lat, lng, radius_km, keywords=None):
        #     api_key = ""
        #     base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        #     params = {
        #         "location": f"{lat},{lng}",
        #         "radius": int(radius_km * 1000),
        #         "key": api_key
        #     }
        #     if keywords:
        #         params["keyword"] = keywords
        #     response = requests.get(base_url, params=params)
        #     if response.status_code != 200:
        #         raise Exception(f"API request failed: {response.text}")
        #     return response.json()
        
        # random_places = []

        # def load_random_places():
        #     try:
        #         lat = random.uniform(8.753515, 20.674545)
        #         lng = random.uniform(72.162216, 80.395555)
        #         keyword = random.choice(['streets', 'houses', 'roads'])
        #         places = get_nearby_places(lat, lng, 100, keyword)['results']
        #         for place in places:
        #             random_places.append({
        #                 'address': place['name'], 
        #                 'location':place['vicinity'].split(', ')[-1], 
        #                 'latitude': place['geometry']['location']['lat'], 
        #                 'longitude': place['geometry']['location']['lng']
        #                 }
        #             )
        #     except Exception as e:
        #         print(e)
        
        # load_random_places()
        # counter = 0

        # def get_random_place(counter):
        #     reset = len(random_places)
        #     if (counter == reset):
        #         load_random_places()
        #         counter = 0
        #         reset = len(random_places)
        #     place = random_places[counter]
        #     counter += 1
        #     return place, counter
            
        # indicator = 0
        # for property_instance in Property.objects.all():
        #     if property_instance.address == 'notLoaded':
        #         indicator += 1
        #         place, counter = get_random_place(counter)
        #         if (place):
        #             property_instance.address = place['address']
        #             property_instance.location = place['location']
        #             property_instance.latitude = place['latitude']
        #             property_instance.longitude = place['longitude']
        #             property_instance.save()
        #         print(indicator)



        def get_random_place():
            # try:
                lat = random.uniform(8.753515, 20.674545)
                lng = random.uniform(72.162216, 80.395555)
                # lat /= 1000000
                # lng /= 1000000
                # keyword = random.choice(['streets', 'houses', 'roads'])
                # places = get_nearby_places(lat, lng, 90, keyword)['results']
                # place = random.choice(places)
                # random_place = {
                #     'address': place['name'], 
                #     'location':place['vicinity'].split(', ')[-1], 
                #     'latitude': place['geometry']['location']['lat'], 
                #     'longitude': place['geometry']['location']['lng']
                # }
                return lat, lng
            # except Exception as e:
            #     print(e)
            #     return None
            
        indicator = 0
        # success = 0
        random_addresses = [
            'MG Road West',
            'South Servaigarar street', 
            'Ashok Nagar road no 1 siripuram', 
            'Cantonment Board Dehu Road', 
            'Omkar chattar farm houses', 
            'Puthen Purackal family houses', 
            'PVMR HOUSES',
            'Near Lakewood Village', 
            "3rd Cross Road, Vaishnavi Nilayam",
            "5th Avenue, Golden Heights",
            "Sunshine Boulevard, Palm Grove",
            "Green Valley, Laurel Lane",
            "Orchid Place, Blossom Street",
            "Silver Crest, Maple Avenue",
            "Royal Gardens, Jasmine Lane",
            "Emerald Court, Cedar Lane",
            "Ivory Towers, Oak Street",
            "Tranquil Terrace, Lily Lane",
            "Coral Springs, Pine Grove",
            'Dargah road East', 
            'Y.V.STREET North',  
            'Lion Empire Street', 
            'The House Design Hub', 
            'AP Transport Unit Office Madanapalle', 
            'Eat Street Goaves', 
            'Fassion Street boutique', 
            'Bajaj Auto (SRR Motors, NH 7 Road)'
        ]
        for property_instance in Property.objects.all():
            if property_instance.address == 'notLoaded':
                indicator += 1
                # place = get_random_place()
                # if (place):
                    # success += 1
                    # property_instance.address = place['address']
                    # property_instance.location = place['location']
                    # property_instance.latitude = place[0]
                    # property_instance.longitude = place[1]
                    # property_instance.save()
                    # print(place[0], place[1])
                # print(indicator, success)
                property_instance.address = random.choice(random_addresses)
                property_instance.save()
        print(indicator)
        
        self.stdout.write(self.style.SUCCESS('Geocodes updated successfully..'))