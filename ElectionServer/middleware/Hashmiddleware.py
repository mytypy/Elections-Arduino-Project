from hashlib import sha256
from django.http import HttpRequest, JsonResponse
from main.models import Hash


class HashMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request: HttpRequest):
        if request.path.startswith('/admin/') or request.path.startswith('/staticfiles/') or request.path.startswith('/static/') or request.path.startswith('/media/') or request.path == '/favicon.ico':
            return self.get_response(request)
        
        validate: bool = self.valid_hash(request)
        
        if validate:
            return self.get_response(request)

        return JsonResponse({'response': 'Тут ничего интересного. Иди отсюда, путник'}, status=403, json_dumps_params={'ensure_ascii': False})

    def valid_hash(self, request: HttpRequest):
        from_base = Hash.objects.get(pk=1)
        hash_header = request.headers.get('Hash', '')
        to_hash = sha256(hash_header.encode()).hexdigest()
        
        return from_base.password == to_hash