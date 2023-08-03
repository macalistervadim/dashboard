from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Административный сайт
    path('admin/', admin.site.urls),
    # Маршруты приложения landing
    path('', include('landing.urls')),
    # CAPTCHA
    path('captcha/', include('captcha.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)