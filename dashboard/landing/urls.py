# Маршрутизация для приложения landing

from django.urls import path

from .views import index, other_page, BBLoginView, profile, BBLogoutView,\
    ProfileEditView, PasswordEditView, RegisterView, RegisterDoneView, \
    user_activate, ProfileDeleteView, PasswordResetView, PasswordReserDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, rubric_bbs, bb_detail,\
    profile_bb_detail, profile_bb_add, profile_bb_delete, profile_bb_edit, comment_delete

app_name = 'landing'
urlpatterns = [
    # Удаление комментария
    path('accounts/profile/comments/delete/<int:pk>/', comment_delete,
         name='profile_comm_del'),
    # Удаление объявления
    path('accounts/profile/delete/<int:pk>/', profile_bb_delete,
         name='profile_bb_delete'),
    # Редактирование объявления
    path('accounts/profile/edit/<int:pk>/', profile_bb_edit,
         name='profile_bb_edit'),
    # Ссылка на добавление объявления
    path('accounts/profile/add/', profile_bb_add, name='profile_bb_add'),
    # Административная ссылка на объявление
    path('accounts/profile/<int:pk>/', profile_bb_detail,
         name='profile_bb_detail'),
    # Сведения о выбранном объявлении
    path('<int:rubric_pk>/<int:pk>/', bb_detail, name='bb_detail'),
    # Рубрики
    path('<int:pk>/', rubric_bbs, name='rubric_bbs'),
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
    # Редактирование профиля
    path('accounts/profile/edit/', ProfileEditView.as_view(),
         name='profile_edit'),
    # Редактирование пароля
    path('accounts/password/edit', PasswordEditView.as_view(),
         name='password_edit'),
    # Сообщение с успешной регистрацией
    path('accounts/register/done/', RegisterDoneView.as_view(),
         name='register_done'),
    # Регистрация пользователя
    path('accounts/register', RegisterView.as_view(), name='register'),
    # Подтверждение почты
    path('accounts/activate/<str:sign>', user_activate, name='activate'),
    # Удаление профиля
    path('accounts/profile/delete/', ProfileDeleteView.as_view(),
         name='profile_delete'),
    # Сброс пароля
    path('accounts/profile/password_reset/', PasswordResetView.as_view(),
         name='password_reset'),
    # Подтверждение сброса пароля
    path('accounts/profile/password_reset/done/', PasswordReserDoneView.as_view(),
         name='pass_reset_done'),
    # Успешный сброс пароля
    path('accounts/profile/password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    # Уведомление об успешном сбросе
    path('accounts/profile/password/reset/complete/', PasswordResetCompleteView.as_view(),
        name='pass_reset_complete'),
]