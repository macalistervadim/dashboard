from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


class AdvUser(AbstractUser):
    """Представление модели пользователя"""
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='Прошел активацию')
    send_messages = models.BooleanField(default=True,
                                        verbose_name='Оповещения')

    class Meta(AbstractUser.Meta):
        pass

class ProfileEditForm(forms.ModelForm):
    """Представление редактирования пользователя"""
    email = forms.EmailField(required=True, label=
                             'Адрес электронной почты')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name',
                  'send_messages')