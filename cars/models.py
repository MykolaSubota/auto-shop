import itertools

from django.db import models


class Part(models.Model):
    class TypePart(models.TextChoices):
        ENGINE = 'EN', 'Двигун'
        GEAR_BOX = 'GB', 'Коробка передач'
        DRIVE = 'DR', 'Привід'
        FUEL_TANK_CAPACITY = 'FT', "Об'єм паливного бака"
        Other = 'OT', 'Інше'

    name = models.CharField('Назва', max_length=50)
    type = models.CharField('Тип', max_length=2, choices=TypePart.choices)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Частина'
        verbose_name_plural = 'Частини'


class CompleteSet(models.Model):
    parts = models.ManyToManyField(Part, verbose_name='Комплектація')

    def __str__(self):
        name = ''

        for part in self.parts.all():
            if part == self.parts.all().last():
                name += part.name
            else:
                name += f'{part.name}-'
        return name

    class Meta:
        verbose_name = 'Комплектація'
        verbose_name_plural = 'Комплектації'


class Auto(models.Model):
    name = models.CharField('Назва', max_length=100)
    complete_sets = models.ManyToManyField(CompleteSet, verbose_name='Комплектації')
    image = models.ImageField(upload_to='images', blank=True, verbose_name='Фотографія')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автомобіль'
        verbose_name_plural = 'Автомобілі'
