import json

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as core_login, logout
from django.http import JsonResponse, HttpResponse


def login(request):
    if request.user.is_active:
        return redirect('home')
    return render(request, 'custom_login/login.html', {})


def do_login(request):
    if request.user.is_active:
        return JsonResponse({ 'status': True })

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        core_login(request, user)
        return JsonResponse({ 'status': True })

    return JsonResponse({'status': False})


def home(request):
    if not request.user.is_active:
        return redirect('/')

    return render(request, 'custom_login/home.html', {
        'data': str(request.user),
    })

def logout_action(request):
    logout(request)
    return redirect('/')
