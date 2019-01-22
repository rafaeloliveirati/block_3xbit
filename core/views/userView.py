from django.http import JsonResponse


def wallet(requests):
    return JsonResponse({'status': 'true'})
