from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import UserModelView


router = SimpleRouter()
router.register(r'user', UserModelView, basename='user')


urlpatterns = [
    path('api/user/', include(router.urls))
]
