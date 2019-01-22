from django.http import JsonResponse


def sendTransaction(requests):
    print(requests)
    return JsonResponse({'status': 'true'})


def findHash(requests):
    print(requests)
    return JsonResponse({'status': 'true'})


def history(requests):
    print(requests)
    return JsonResponse({'status': 'true'})


def receivedTransaction(requests):
    print(requests)
    return JsonResponse({'status': 'true'})
