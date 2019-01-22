from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from core.models.models import User


@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        users = User.objects.filter(email=email, password=password)
        if users:
            return render(request, "home.html")
        else:
            return HttpResponse("Authentication failed", status=401)


@csrf_exempt
def register(request):
    if request.method == 'GET':
        return render(request, "register.html")
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User(email=email, password=password)
        if User.objects.filter(email=email):
            return render(request, "login.html")
        user.save()
        return HttpResponse("Register done with success", status=200)
