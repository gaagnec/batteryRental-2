from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'список клиентов'

    def __str__(self):
        return self.name


class Payment(models.Model):
    id = models.UUIDField(primary_key=True)
    user_id = models.UUIDField()
    client_id = models.UUIDField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'payments'
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'

    def __str__(self):
        return f"Платеж {self.id} - {self.amount}"
