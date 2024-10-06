from django.db import models
from django.contrib.auth.models import AbstractUser


class ElectionModel(models.Model):

    name = models.CharField(verbose_name='Имя', max_length=256)


class UserModel(AbstractUser):
    id_card = models.CharField(max_length=256, verbose_name='ID карточки')