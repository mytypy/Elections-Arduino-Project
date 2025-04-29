from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('election.urls')),
    path('', include('choice.urls'))
]


admin.site.site_header = 'Администрирование голосований'