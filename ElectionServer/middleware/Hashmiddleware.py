from hmac import compare_digest
from django.http import HttpRequest, JsonResponse
from models.models import SecretKey


class HashMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request: HttpRequest):
        if request.path.startswith('/admin/') or request.path.startswith('/staticfiles/') or request.path.startswith('/static/') or request.path.startswith('/media/') or request.path == '/favicon.ico':
            return self.get_response(request)

        secret = SecretKey()
        data: dict = request.headers
        
        client_key = data.get('Hash', ' ')

        if not compare_digest(client_key, secret.SECRET):
            return JsonResponse({'detail': 'Подпись не совпадает!'}, json_dumps_params={'ensure_ascii': False}, status=403)

        return self.get_response(request)

