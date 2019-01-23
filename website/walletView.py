import json

import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from block_3xbit.models import User

root_url = 'https://api.blockcypher.com/v1/btc/test3'
create_addres_url = root_url + '/addrs'
create_wallet_url = root_url + "/wallets?token=57c3f60a4cb04c019b39ef2853a1c603"
token = '57c3f60a4cb04c019b39ef2853a1c603'
headers = {
    'Content-Type': 'application/json',
}


@csrf_exempt
def createWallet(request):
    user = User.objects.filter(email=request.POST.get('email')).first()
    if not user.source_addres:
        address_response = requests.post(create_addres_url, data={})
        content = json.loads(address_response.content)
        user.source_addres = content['address']
    if not user.wallet_name:
        data = {
            "name": request.POST.get('wallet_name'),
            "addresses": [user.source_addres]
        }
        requests.post(create_wallet_url, headers=headers, data=json.dumps(data))
        user.wallet_name = request.POST.get('wallet_name')
    user.save()
    return JsonResponse({'status': 'true'})
