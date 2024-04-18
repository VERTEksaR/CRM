from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render


def login_view(request: HttpRequest) -> HttpResponse:
    """Функция для аутентификации пользователей на сайте"""
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('')
        return render(request, 'auth/login.html')

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user:
        login(request, user)
        return redirect('')
    return render(request, 'auth/login.html', {'error': 'Invalid login credentials'})


def logout_view(request: HttpRequest) -> HttpResponse:
    """Функция для разлогирования пользователей на сайте"""
    logout(request)
    return redirect('/')
