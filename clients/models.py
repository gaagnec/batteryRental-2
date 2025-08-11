from django.db import models
import uuid

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    created_at = models.DateTimeField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'clients'
        verbose_name = 'клиент'
        verbose_name_plural = 'список клиентов'

    def __str__(self):
        return self.name

class Payment(models.Model):
    id = models.UUIDField(primary_key=True)
    rental_id = models.UUIDField()
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='client_id')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50)
    method = models.CharField(max_length=50)
    paid_at = models.DateTimeField()
    note = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'payments'
        managed = False

    def __str__(self):
        return f"Payment {self.id} - Client: {self.client_id.name}"