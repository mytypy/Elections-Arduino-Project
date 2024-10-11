from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ElectionModelView


router = SimpleRouter()
router.register(r'election', ElectionModelView, basename='election')


urlpatterns = [
    path('api/', include(router.urls))
]
