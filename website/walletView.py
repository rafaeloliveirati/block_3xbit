import hashlib
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from block_3xbit.models import User
import requests

rootUrl = 'https://api.blockcypher.com/v1/btc/test3/addrs'
token = '57c3f60a4cb04c019b39ef2853a1c603'


@csrf_exempt
def createWallet(request):
    # Buscar o email do usuario logado
    # user = User.objects.filter(email='rafael').first()
    user = User.objects.filter(email=request.POST.get('email')).first()
    if user.source_addres:
        # Cria Wallet
        source_adress = user.source_addres
    else:
        response = requests.post(rootUrl, data={})
        content = json.loads(response.content)
        user.source_addres = content['address']
        user.save()
    return JsonResponse({'status': 'true'})
