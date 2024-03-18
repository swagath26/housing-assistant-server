from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('properties_list', views.PropertyViewSet)

urlpatterns = [
    path('add/', views.addProperty, name = 'add'),
]
urlpatterns += router.urls