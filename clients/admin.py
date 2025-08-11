from django.contrib import admin
from .models import Client, Payment


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'client_id', 'amount', 'payment_type', 'payment_method', 'payment_date', 'description')
