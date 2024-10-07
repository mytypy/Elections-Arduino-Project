from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import Election, UserModelView


router = SimpleRouter()
router.register(r'user', UserModelView, basename='user')
print(router.urls)

urlpatterns = [
    path('api/v8/elction/<int:pk>/',  Election.as_view()),
    path('api/v8/', include(router.urls))
]
