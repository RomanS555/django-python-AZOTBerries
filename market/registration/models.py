from django.db import models 
from django.utils import timezone
from django.db.models import JSONField

class ShopUser(models.Model):
    login = models.CharField('Логин', max_length=12)
    password = models.CharField('Пароль', max_length=32)
    date_of_creation = models.DateTimeField('Дата регистрации',default=timezone.now)
    user_products =  JSONField(
        default=list, 
        blank=True,
        null=True
    )
    def __str__(self):
        return self.login
