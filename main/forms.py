from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['location', 'address', 'description', 'price', 'bedrooms', 'bathrooms', 'balcony', 'area', 'home_type']