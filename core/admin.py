from django.contrib import admin
from .models import Factory, Unit, Equipment


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'factory')
    list_filter  = ('factory',)
    search_fields = ('name',)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    filter_horizontal = ('units',)
    search_fields = ('name',)
