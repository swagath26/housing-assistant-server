from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .forms import RegisterForm
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.middleware.csrf import get_token
from django.contrib.auth.models import User

def get_user(request):
    user = request.user
    user_details = {
        "first_name": user.first_name,
        "last_name": user.last_name
    }
    return JsonResponse(user_details)

# @csrf_protect
def get_csrftoken(request):
    token = get_token(request)
    response = JsonResponse({'csrftoken':token})
    return response

def check_username(request):
    if request.method == 'GET':
        username = request.GET.get('username', None)
        if username is not None:
            try:
                User.objects.get(username=username)
                availability = False
            except User.DoesNotExist:
                availability = True
            return JsonResponse({'availability':availability})
        else:
            return JsonResponse({'availability':False})

def signin_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me')
        user = authenticate(username = username, password=password)
        if user is not None:
            login(request, user)
            response = JsonResponse({
                'success': True, 
                'messages': "Signed in successfully",
                })
            duration = 600
            if remember_me == "true":
                duration = 3600
            response.set_cookie('is_authenticated', True, max_age=duration)
            response.set_cookie('username', user.username, max_age=duration)
            return response
        else:
            try:
                User.objects.get(username=username)
                availability = True
            except User.DoesNotExist:
                availability = False
                return JsonResponse({'success':False, 'errors': "username"})
            if(availability):
                return JsonResponse({'success':False, 'errors': "password"})
    
def signout_user(request):
    logout(request)
    response = JsonResponse({'success':True, 'messages': "Signed out successfully"})
    if 'is_authenticated' in request.COOKIES:
        response.delete_cookie('is_authenticated')
        response.delete_cookie('user')
    return response

@ensure_csrf_cookie
def signup_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        remember_me = request.POST.get('remember_me')
        if form.is_valid():
            user = form.save()
            login(request, user)
            response = JsonResponse({
                'success':True, 
                'messages': "User registered successfully",
                })
            duration = 600
            if remember_me == "true":
                duration = 3600
            response.set_cookie('is_authenticated', True, max_age=duration)
            response.set_cookie('username', user.username, max_age=duration)
            return response
        else:
            return JsonResponse({'success':False, 'errors': form.errors})