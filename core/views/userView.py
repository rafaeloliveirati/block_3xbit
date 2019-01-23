import hashlib

from django.http import JsonResponse

rootUrl = "https://api.blockcypher.com/v1/btc/test3/addrs"
token = '57c3f60a4cb04c019b39ef2853a1c603'


def wallet(request):
    m = hashlib.sha256()
    m.update(b"Nobody inspects")
    print(m.hexdigest())
    # hash = "transaction_message_hex"
    # hashcode = hashlib.sha256(hashlib.sha256(hash.hexdigest()).digest()).hexdigest()
    return JsonResponse({'status': 'true'})
