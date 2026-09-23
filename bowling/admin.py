from django.contrib import admin

from bowling.models import Client
from bowling.models import Booking
from bowling.models import Lane
from bowling.models import Service
from bowling.models import BookinAndService
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'telephone', 'Date_birth', 'Loyalty_status']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'start_time', 'end_time', 'price', 'status', 'client__id', 'lane__id']

@admin.register(Lane)
class LaneAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'kind', 'status', 'price']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'сategory', 'price', 'unit_measurement']

@admin.register(BookinAndService)
class BookinAndServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'quantity', 'price_moment_order', 'sum', 'booking__id', 'service__id']    