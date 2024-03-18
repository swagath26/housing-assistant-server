from django.urls import path
from . import views

urlpatterns = [
    path('get-user/', views.get_user, name="get-user"),
    path('check-username/', views.check_username, name="check-username"),
    path('get-csrftoken/', views.get_csrftoken, name="get_csrftoken"),
    path('signup/', views.signup_user, name="signup"),
    path('signin/', views.signin_user, name="signin"),
    path('signout/', views.signout_user, name="signout"),
]