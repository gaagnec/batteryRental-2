from django.contrib import admin
from .models import Client, Payment

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'rental_id', 'client_id', 'client_name', 'amount', 'type', 'method', 'paid_at', 'note')

    def client_name(self, obj):
        return obj.client_id.name
    client_name.short_description = 'Имя клиента'
