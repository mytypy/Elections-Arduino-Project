from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ChoiceViewSet


router = SimpleRouter()
router.register(r'choice', ChoiceViewSet, basename='choice')


urlpatterns = [
    path('api/', include(router.urls))
]
