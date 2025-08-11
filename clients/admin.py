from django.contrib import admin
from .models import Client, Payment


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'rental_id', 'client_id', 'amount', 'type', 'method', 'paid_at', 'note')
