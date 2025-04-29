from django.db import models


class ElectionModel(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=254, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания', null=True)    
    
    class Meta:
        verbose_name = 'Голосования'
        verbose_name_plural = 'Голосования'
        
    def __str__(self) -> str:
        return self.name