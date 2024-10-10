from django.db import models


class ElectionModel(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=256)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания', null=True)    
    
    def __str__(self) -> str:
        return self.name