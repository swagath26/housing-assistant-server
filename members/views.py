from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
from django.http import JsonResponse
from .forms import RegisterForm
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.middleware.csrf import get_token

@csrf_protect
def get_csrftoken(request):
    token = get_token(request)
    response = JsonResponse({'csrftoken':token})
    return response

def signin_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me')
        user = authenticate(username = username, password=password)
        if user is not None:
            login(request, user)
            response = JsonResponse({
                'success':True, 
                'messages': "Signed in successfully",
                })
            if remember_me == "true":
                response.set_cookie('is_authenticated', True, max_age=3600)
                response.set_cookie('user', {
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                }, max_age=3600)
            return response
        else:
            return JsonResponse({'success':False, 'messages': "Invalid username or password!"})

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
        if form.is_valid():
            username = request.POST.get('username')
            user = form.save()
            login(request, user)
            return JsonResponse({'success':True, 'messages': "User registered successfully"}).set_cookie('username', username)
        else:
            return JsonResponse({'success':False, 'errors': form.errors})

def forgot_password(request):
    pass

# remember me