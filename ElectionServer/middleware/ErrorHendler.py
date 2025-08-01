from rest_framework.views import exception_handler as drf_default_handler
from rest_framework.response import Response
from main.error import HttpError


def custom_exception_handler(exc, context):
    if isinstance(exc, HttpError):
        return Response(
            {"detail": exc.detail},
            status=exc.status_code
        )
    
    return drf_default_handler(exc, context)