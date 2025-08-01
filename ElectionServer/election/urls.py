from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ElectionViewSet


router = SimpleRouter()
router.register(r'election', ElectionViewSet, basename='election')


urlpatterns = [
    path('api/', include(router.urls))
]
