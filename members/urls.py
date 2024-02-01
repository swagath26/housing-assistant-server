from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('get-users', views.UserViewSet)

urlpatterns = [
    path('get-user/', views.get_user, name="get-user"),
    path('get-csrftoken/', views.get_csrftoken, name="get_csrftoken"),
    path('signup/', views.signup_user, name="signup"),
    path('signin/', views.signin_user, name="signin"),
    path('forgot-password/', views.forgot_password, name="forgot-password"),
    path('signout/', views.signout_user, name="signout"),
]

# urlpatterns += router.urls