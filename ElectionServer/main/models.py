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
    
# list(ChoiceModel.objects.filter(election_id=4).values('name').annotate(votes=Count('user'))) -> [{'name': 'Да', 'votes': 51}, {'name': 'Нет', 'votes': 49}]