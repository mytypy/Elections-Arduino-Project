from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import UserModelView, ElectionModelView


router = SimpleRouter()
router.register(r'user', UserModelView, basename='user')
router.register(r'election', ElectionModelView, basename='election')

urlpatterns = [
    path('api/v8/', include(router.urls))
]
