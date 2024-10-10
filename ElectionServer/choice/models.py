from django.db import models


class ChoiceModel(models.Model):
    name = models.CharField(max_length=254, verbose_name='Имя выбора', unique=True)
    election = models.ForeignKey(
        'election.ElectionModel',
        on_delete=models.CASCADE,
        related_name='choices',
        verbose_name='Голосования',
        null=True
    )
    
    def __str__(self) -> str:
        return self.name