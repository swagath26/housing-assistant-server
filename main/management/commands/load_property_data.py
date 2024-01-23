from django.core.management.base import BaseCommand
from main.models import Property
import pandas as pd
import os

class Command(BaseCommand):
    help = 'Load data into the database'

    def handle(self, *args, **option):

        this_file_path = os.path.abspath(__file__)
        this_dir = os.path.dirname(this_file_path)
        prev_dir = os.path.dirname(this_dir)
        base_dir = os.path.dirname(prev_dir)
        file_rel_path = 'data/Bengaluru_House_Data.csv'
        file_path = os.path.join(base_dir, file_rel_path)
        df = pd.read_csv(file_path)
        df.dropna(inplace=True)
        
        
        for index, row in df.iterrows():
            Property.objects.create(
                area_type = row['area_type'],
                availability = row['availability'],
                location = row['location'],
                size = row['size'],
                society = row['society'],
                area = row['total_sqft'],
                bathrooms = row['bath'],
                balcony = row['balcony'],
                price = row['price'],
            )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully..'))