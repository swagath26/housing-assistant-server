from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse

def signin_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username = "swakkidi", password=password)
        if user is not None:
            login(request, user)
            print("hehe")
            return JsonResponse({'success':True, 'messages': "Signed in successfully"})
        else:
            print("hihi")
            return JsonResponse({'success':False, 'messages': "Sign in failed"})

def signout_user(request):
    logout(request)
    print("signed out")
    return JsonResponse({'success':True, 'messages': "Signed out successfully"})

def signup_user(request):
    pass

def forgot_password(request):
    pass

# remember me