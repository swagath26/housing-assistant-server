from .models import Property, PropertyImage
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core import serializers
# from django.views.decorators import login_required
from rest_framework import viewsets, filters, pagination
from .serializers import PropertySerializer
from .forms import PropertyForm
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, NumberFilter

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class PropertyFilter(FilterSet):
    min_price = NumberFilter(field_name="price", lookup_expr='gte')
    max_price = NumberFilter(field_name="price", lookup_expr='lte')
    min_area = NumberFilter(field_name='area', lookup_expr='gte')
    max_area = NumberFilter(field_name='area', lookup_expr='lte')

    class Meta:
        model=Property
        fields=['bedrooms', 'id']

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    # pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_class = PropertyFilter
    search_fields = ['location', 'address', 'area_type']
    ordering_fields = ['price', 'bedrooms']

# def getProperty(request):
#     queryset = Property.objects.all()
#     data = serializers.serialize('json', queryset)
#     return JsonResponse({'data':data})
        
# @login_required(login_url='/members/signin/')
# @ensure_csrf_cookie
def addProperty(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.owner = request.user
            property.save()
            images = request.FILES.getlist('images')
            for image in images:
                PropertyImage.objects.create(property=property, image=image)
            return JsonResponse({'success':True, 'message': "Property added successfully"})
        else:
            return JsonResponse({'success':False, 'errors': form.errors})
        

# @login_required(login_url='/members/signin/')
@ensure_csrf_cookie
def deleteProperty(request):
    if request.method == 'POST':
        property_id = request.POST.get("id")
        property = Property.objects.filter(id=property_id).first()
        if property:
            if property.owner == request.user:
                property.delete()
                return JsonResponse({'success':True, 'message': "Property deleted successfully"})
            else:
                return JsonResponse({'success':False, 'errors': "You are not the owner of the property"})
        else:
            return JsonResponse({'success':False, 'errors': "Property does not exist"})
        
# @login_required(login_url='/members/signin/')
@ensure_csrf_cookie
def editProperty(request):
    if request.method == 'POST':
        property_id = request.POST.get("id")
        property = Property.objects.filter(id=property_id).first()
        if property:
            if property.owner == request.user:
                form = PropertyForm(request.POST)
                if form.is_valid():
                    property_updated = form.save(commit=False)
                    property_updated.owner = request.user
                    property_updated.save()
                    images = request.FILES.getlist('images')
                    for image in images:
                        PropertyImage.objects.create(property=property_updated, image=image)
                    property.delete()
                    return JsonResponse({'success':True, 'messages': "Property updated successfully"})
                else:
                    return JsonResponse({'success':False, 'errors': form.errors})
            else:
                return JsonResponse({'success':False, 'errors': "You are not the owner of this property"})
        else:
            return JsonResponse({'success':False, 'errors': "Property does not exist"})