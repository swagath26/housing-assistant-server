from django.core.management.base import BaseCommand
from main.models import Property
from django.contrib.auth.models import User
import pandas as pd
import os
import random

class Command(BaseCommand):
    help = 'Load data into the database'

    def handle(self, *args, **option):

        this_file_path = os.path.abspath(__file__)
        this_dir = os.path.dirname(this_file_path)
        prev_dir = os.path.dirname(this_dir)
        base_dir = os.path.dirname(prev_dir)
        file_rel_path = 'data/Property_Data.csv'
        file_path = os.path.join(base_dir, file_rel_path)
        df = pd.read_csv(file_path)
        df.dropna(inplace=True)
        
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
        
        for index, row in df.iterrows():
            Property.objects.create(
                owner = User.objects.get(username = 'admin'),
                location = 'Random Location',
                address = random.choice(random_addresses),
                description = row['description'],
                price = row['price'],
                bedrooms = row['bedrooms'],
                bathrooms = row['bathrooms'],
                balcony = row['balcony'],
                area = row['area'],
                area_type = row['area_type'],
                # date_of_availability = row['availability'],
                ready_to_move = False
            )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully..'))