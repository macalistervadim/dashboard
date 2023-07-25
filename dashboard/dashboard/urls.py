from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Административный сайт
    path('admin/', admin.site.urls),
    # Маршруты приложения landing
    path('', include('landing.urls')),
]
