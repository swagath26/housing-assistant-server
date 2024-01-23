from django.core.management.base import BaseCommand
from main.models import PropertyImage

class Command(BaseCommand):
    help = 'Delete Property Image Data from the database'

    def handle(self, *args, **option):

        PropertyImage.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Property Image Data deleted successfully..'))