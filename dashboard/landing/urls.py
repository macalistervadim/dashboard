# Маршрутизация для приложения landing

from django.urls import path

from .views import index, other_page

app_name = 'landing'
urlpatterns = [
    # Вспомогательные страницы
    path('<str:page>/', other_page, name='other'),
    # Главная страница
    path('', index, name='index'),
]