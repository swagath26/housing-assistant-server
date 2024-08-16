# ----------- views.py ----------------
# 
# from .models import PropertyImage
# from django.http import JsonResponse
# from django.views.decorators.csrf import ensure_csrf_cookie
# from django.contrib.auth.decorators import login_required
# from .forms import PropertyForm
# from django_filters.rest_framework import BaseInFilter

# class NumberInFilter(BaseInFilter, NumberFilter):
#     pass

# class CharInFilter(BaseInFilter, CharFilter):
#     pass

#     beds = NumberInFilter(field_name='bedrooms', lookup_expr='in')
#     type = CharInFilter(field_name='home_type', lookup_expr='in')

# @login_required
# @ensure_csrf_cookie
# def addProperty(request):
#     if request.method == 'POST':
#         form = PropertyForm(request.POST)
#         if form.is_valid():
#             property = form.save(commit=False)
#             user = request.user
#             if user is not None:
#                 property.owner = user
#                 property.save()
#                 images = request.FILES.getlist('images')
#                 for image in images:
#                     PropertyImage.objects.create(property=property, image=image)
#                 return JsonResponse({'success':True, 'message': "Property added successfully"})
#             else:
#                 return JsonResponse({'success':False, 'errors': 'User not authenticated'})
#         else:
#             return JsonResponse({'success':False, 'errors': form.errors})

# ----------- forms.py ----------------

# from django import forms
# from .models import Property

# class PropertyForm(forms.ModelForm):
#     class Meta:
#         model = Property
#         fields = ['location', 'address', 'description', 'price', 'bedrooms', 'bathrooms', 'balcony', 'area', 'home_type']