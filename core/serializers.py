# core/serializers.py
from rest_framework import serializers
from .models import Factory, Unit, Equipment

class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = ('id', 'name')

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'name', 'factory')

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id', 'name', 'units')
