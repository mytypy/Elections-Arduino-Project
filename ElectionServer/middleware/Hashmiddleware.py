from hashlib import sha256
from django.http import HttpResponse, HttpRequest, JsonResponse
from main.models import Hash


class HashMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request: HttpRequest):
        response: HttpResponse = self.get_response(request)
        from_base = Hash.objects.get(pk=1)
        
        hash_header = request.headers.get('Hash', '')
        to_hash = sha256(hash_header.encode()).hexdigest()

        if to_hash == from_base.password:
            return response
        
        return JsonResponse({'response': 'Тут ничего интересного. Иди отсюда, путник'}, status=403, json_dumps_params={'ensure_ascii': False})