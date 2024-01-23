from django.core.management.base import BaseCommand
from main.models import Property

class Command(BaseCommand):
    help = 'Delete data into the database'

    def handle(self, *args, **option):

        Property.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Data deleted successfully..'))