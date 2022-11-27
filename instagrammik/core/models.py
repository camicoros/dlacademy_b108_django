from django.contrib.auth.models import AbstractUser
from django.db import models


"""
наследуемся от AbstractUser, 
чтобы создать свою собственную модель пользователя

AbstractUser включает в себя весь необходимый функционал для работы с админкой
стандартная модель пользователя Django так же наследуется от него

!!! не забудьте в settings.py поменять стандартную модель пользователя на новую
AUTH_USER_MODEL = 'core.CustomUser'

для работы с изображениями нужно будет дополнительно поставить библиотеку Pillow
pip install Pillow
"""


def user_avatar_path(instance, filename):
    user_id = instance.id
    return "user_avatars/user-{}/{}".format(user_id, filename)


class CustomUser(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    about = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to=user_avatar_path)
    friends = models.ManyToManyField('self', blank=True)
