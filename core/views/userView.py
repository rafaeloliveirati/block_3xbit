from django.http import JsonResponse, HttpResponse

from core.models.models import User


def login(requests):
    user = User.objects.filter(name='rafael')
    return HttpResponse(user.email)


def register(requests):
    user = User(name='rafael', email='teste@teste.com.')
    user.save()
    return JsonResponse({'status': 'true'})


def wallet(requests):
    return JsonResponse({'status': 'true'})
