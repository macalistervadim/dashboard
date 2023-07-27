from django.db import models
from django.contrib.auth.models import AbstractUser

class AdvUser(AbstractUser):
    """Представление модели пользователя"""
    is_actived = models.BooleanField(default=True, db_index=True,
                                     verbose_name='Прошел активацию')
    send_messages = models.BooleanField(default=True,
                                        verbose_name='Оповещения')

    class Meta(AbstractUser.Meta):
        pass
