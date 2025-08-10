from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'список клиентов'

    def __str__(self):
        return self.name
