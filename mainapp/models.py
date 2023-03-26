from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Feedback(models.Model):
    date = models.DateTimeField(
        'Дата создания',
        default=timezone.now
    )
    phone = PhoneNumberField(
        verbose_name=('Телефон'),
        max_length=15,
        unique = True,
        null = False,
        blank = False,
        help_text='Введите телефонный номер'
    )
    email = models.EmailField(
        max_length=254,
        null = False,
        blank = False,
        help_text='Введите адрес электронной почты')
    name = models.CharField(
        'Имя',
        max_length=200,
        help_text='Введите ваше имя'
    )
    message = models.TextField(
        'Сообщение',
        help_text='Напишите сообщение'
    )
  