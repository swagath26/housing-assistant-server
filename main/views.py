from .models import Property, PropertyImage
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
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
        fields=['size']

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_class = PropertyFilter
    search_fields = ['location', 'society', 'area_type']
    ordering_fields = ['price', 'size']

@ensure_csrf_cookie
def addProperty(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save()
            images = request.FILES.getlist('images')
            for image in images:
                PropertyImage.objects.create(property=property, image=image)
            return JsonResponse({'success':True, 'message': "Property added successfully"})
        else:
            return JsonResponse({'success':False, 'errors': form.errors})