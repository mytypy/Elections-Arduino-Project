from django.http import HttpResponse, HttpRequest, JsonResponse


class HashMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request: HttpRequest):
        response: HttpResponse = self.get_response(request)
        
        hash_header = request.headers.get('X-Hash')
        
        # if hash_header == '':
        #     return response
        
        # return JsonResponse({'response': 'Тут ничего интересного. Иди отсюда, путник'}, status=403)
        return response
