from django.db import models

# Create your models here.
# каждый класс соответствует таблицам базы данных

class Product(models.Model):
    name = models.CharField('Название', help_text="Здесь введите название товара", max_length=30)
    desc = models.TextField('Описание', null=True)
    cost = models.FloatField('Цена')
    slug = models.SlugField(max_length=50)
    active = models.BooleanField('Активный', default=False)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def cap_name(self):
        return self.name.upper()