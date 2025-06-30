from django.db import models


# core/models.py

from django.db import models

class Factory(models.Model):
    name = models.CharField('Название фабрики', max_length=100, unique=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField('Название участка', max_length=100)
    factory = models.ForeignKey(
        Factory, on_delete=models.CASCADE,
        related_name='units', verbose_name='Фабрика'
    )

    def __str__(self):
        return f"{self.factory.name} → {self.name}"


class Equipment(models.Model):
    name = models.CharField('Тип оборудования', max_length=100)
    units = models.ManyToManyField(
        Unit, related_name='equipment',
        verbose_name='Принадлежит участкам'
    )

    def __str__(self):
        return self.name

