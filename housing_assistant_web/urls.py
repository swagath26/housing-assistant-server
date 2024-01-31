from django.contrib import admin
from django.urls import path, include
from main.views import addProperty, PropertyViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('properties_list', PropertyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', addProperty, name = 'add'),
    # path('get_list/', getProperty, name = 'get_list'),
    # path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]

urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)