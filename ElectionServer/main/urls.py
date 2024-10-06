from django.contrib import admin
from django.urls import path
from .views import Election


urlpatterns = [
    path('api/v8/elction/<int:pk>/',  Election.as_view()),
]
