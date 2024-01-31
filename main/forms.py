from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['location', 'address', 'description', 'price', 'bedrooms', 'bathrooms', 'balcony', 'area', 'area_type', 'date_of_availability', 'ready_to_move']