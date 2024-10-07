from django.db import models


class ElectionModel(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=256)
    
    def __str__(self) -> str:
        return self.name
    
class ChoiceModel(models.Model):
    name = models.CharField(max_length=254, verbose_name='Имя выбора', unique=True)
    election = models.ForeignKey(
        ElectionModel,
        on_delete=models.PROTECT,
        related_name='choices',
        verbose_name='Голосования'
    )
    
    def __str__(self) -> str:
        return self.name


class UserModel(models.Model):
    id_card = models.CharField(max_length=254, verbose_name='ID карточки', unique=True)
    election = models.ForeignKey(ElectionModel,
                                 on_delete=models.PROTECT,
                                 related_name='user',
                                 verbose_name='Голосования',
                                 null=True)
    choice = models.ForeignKey(
        ChoiceModel,
        on_delete=models.PROTECT,
        related_name='user',
        verbose_name='Выборы ответов',
        null=True
    )