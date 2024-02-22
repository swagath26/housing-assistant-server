from django.core.management.base import BaseCommand
from main.models import Property
from django.contrib.auth.models import User
import pandas as pd
import os

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
        
        
        for index, row in df.iterrows():
            Property.objects.create(
                owner = User.objects.get(username = 'admin'),
                location = 'notLoaded',
                address = 'notLoaded',
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