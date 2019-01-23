from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from block_3xbit.models import User


@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, "website/login.html")
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email, password=password).first()
        if user:
            context = {
                'user': user
            }
            return render(request, "website/home.html", context)
        else:
            return HttpResponse("Authentication failed", status=401)


@csrf_exempt
def register(request):
    if request.method == 'GET':
        return render(request, "website/register.html")
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User(email=email, password=password)
        if User.objects.filter(email=email):
            return render(request, "website/login.html")
        user.save()
        return render(request, "website/login.html")
