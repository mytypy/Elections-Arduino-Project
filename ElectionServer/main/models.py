from django.db import models


class UserModel(models.Model):
    id_card = models.CharField(max_length=254, verbose_name='ID карточки', unique=True)
    election = models.ForeignKey('election.ElectionModel',
                                 on_delete=models.CASCADE,
                                 related_name='user',
                                 verbose_name='Голосования',
                                 null=True)
    choice = models.ForeignKey(
        'choice.ChoiceModel',
        on_delete=models.CASCADE,
        related_name='user',
        verbose_name='Выборы ответов',
        null=True
    )
    
    def __str__(self):
        return self.id_card
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Hash(models.Model):
    password = models.CharField(max_length=255, verbose_name='Хэш', unique=True)