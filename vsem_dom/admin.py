from django.contrib import admin

from .models import Agent, Client, Property, Deal, Status_deal


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    fields = ('name', 'surname', 'phone_number', 'email')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fields = ('name', 'surname', 'phone_number', 'email')


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    fields = ('property_type', 'address', 'rooms', 'area', 'price')


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    fields = ('agent_id', 'client_id', 'property_id', 'deal_date', 'deal_amount')


@admin.register(Status_deal)
class Status_dealAdmin(admin.ModelAdmin):
    fields = ('status',)
