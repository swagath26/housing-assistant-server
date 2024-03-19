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

        addr_list = [
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

        desc_list = [
            "Experience the epitome of modern luxury in this spacious penthouse apartment, featuring floor-to-ceiling windows, a gourmet kitchen, and a private rooftop terrace with stunning city views.",
            "Discover coastal living at its finest in this charming beachfront cottage, boasting sun-drenched rooms, hardwood floors, and direct access to pristine sandy shores for endless seaside adventures.",
            "Indulge in resort-style living in this exclusive gated community, offering a championship golf course, clubhouse amenities, and lush landscaped grounds perfect for leisurely strolls.",
            "Escape to the countryside with this picturesque farmhouse retreat, where rolling hills, tranquil ponds, and acres of open space provide the ideal setting for a peaceful rural lifestyle.",
            "Step into elegance with this historic Victorian mansion, featuring intricate architectural details, grand living spaces, and manicured gardens reminiscent of a bygone era.",
            "Savor the tranquility of mountain living in this stunning log cabin, nestled among towering pine trees and offering panoramic views of snow-capped peaks from every window.",
            "Live the waterfront dream in this sleek contemporary villa, boasting a private boat dock, infinity pool, and expansive outdoor living spaces overlooking the shimmering waters of the bay.",
            "Immerse yourself in nature in this eco-friendly retreat, where sustainable design, native landscaping, and off-the-grid amenities combine to create a harmonious sanctuary in the wilderness.",
            "Find serenity in this Zen-inspired oasis, featuring a Japanese garden, meditation room, and tranquil water features designed to promote relaxation and mindfulness.",
            "Unwind in style in this urban loft apartment, with exposed brick walls, industrial-chic furnishings, and skyline views creating a hip and vibrant downtown living experience.",
        ]

        
        for index, row in df.iterrows():
            Property.objects.create(
                owner = User.objects.get(username = 'admin'),
                location = 'Random Location',
                address = random.choice(addr_list),
                description = random.choice(desc_list),
                price = row['price'],
                bedrooms = row['bedrooms'],
                bathrooms = row['bathrooms'],
                balcony = row['balcony'],
                area = row['area'],
                home_type = row['home_type'],
                latitude = random.uniform(8.753515, 20.674545),
                longitude = random.uniform(72.162216, 80.395555),
            )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully..'))