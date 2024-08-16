from .models import Property, PropertyImage
from .serializers import PropertySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination

from django_filters import FilterSet, NumberFilter, CharFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class PropertyPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 500

class PropertyFilter(FilterSet):
    min_price = NumberFilter(field_name="price", lookup_expr='gte')
    max_price = NumberFilter(field_name="price", lookup_expr='lte')
    min_lat = NumberFilter(field_name="latitude", lookup_expr='gte')
    max_lat = NumberFilter(field_name="latitude", lookup_expr='lte')
    min_lng = NumberFilter(field_name="longitude", lookup_expr='gte')
    max_lng = NumberFilter(field_name="longitude", lookup_expr='lte')
    min_area = NumberFilter(field_name='area', lookup_expr='gte')
    max_area = NumberFilter(field_name='area', lookup_expr='lte')
    min_bed = NumberFilter(field_name='bedrooms', lookup_expr='gte')
    min_bath = NumberFilter(field_name='bathrooms', lookup_expr='gte')

    beds = CharFilter(field_name='bedrooms', lookup_expr='in', method='filter_by_bedrooms')
    type = CharFilter(field_name='home_type', lookup_expr='in', method='filter_by_type')

    class Meta:
        model=Property
        fields = ['min_price', 'max_price', 'min_lat', 'max_lat', 'min_lng', 'max_lng', 
                  'min_area', 'max_area', 'min_bed', 'min_bath', 'type', 'beds', 'bathrooms']
        
    def filter_by_type(self, queryset, name, value):
        home_types = value.split(',')
        return queryset.filter(home_type__in=home_types)
    
    def filter_by_bedrooms(seld, queryset, name, value):
        bedrooms_list = value.split(',')
        return queryset.filter(bedrooms__in=bedrooms_list)

class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PropertyPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PropertyFilter
    search_fields = ['location', 'address', 'home_type']
    ordering_fields = ['price', 'bedrooms']
    ordering = ['-id']

    def perform_create(self, serializer):
        property_instance = serializer.save(owner=self.request.user)
        images = self.request.FILES.getlist('images')
        for image in images:
            PropertyImage.objects.create(property=property_instance, image=image)
