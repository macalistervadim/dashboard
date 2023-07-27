# Маршрутизация для приложения landing

from django.urls import path

from .views import index, other_page, BBLoginView, profile, BBLogoutView

app_name = 'landing'
urlpatterns = [
    # Вспомогательные страницы
    path('<str:page>/', other_page, name='other'),
    # Главная страница
    path('', index, name='index'),
    # Страница входа
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    # Страница профиля пользователя
    path('accounts/profile/', profile, name='profile'),
    # Выход с профиля
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
]