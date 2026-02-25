from django.db import models


class Product(models.Model):
    title = models.CharField('Название', max_length=64)
    description = models.CharField('Описание', max_length=1024)
    
    def __str__(self):
        return self.title
