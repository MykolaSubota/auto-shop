from django.contrib.auth.models import AbstractUser
from django.db import models
from cars.models import Auto
from django.contrib.auth import get_user_model
from cars.models import Part


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return self.username


class Order(models.Model):
    last_name = models.CharField('Прізвище', max_length=80)
    first_name = models.CharField("Ім'я", max_length=80)
    email = models.EmailField('Електронна пошта')
    phone = models.CharField('Номер телефону', max_length=15)
    auto = models.OneToOneField(Auto, models.PROTECT, verbose_name='Автмобіль')
    parts = models.ManyToManyField(Part, 'Частини')
    manager = models.OneToOneField(get_user_model(), on_delete=models.PROTECT, verbose_name='Менеджер')
    note = models.TextField('Примітка', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.auto}'

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
