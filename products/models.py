from django.db import models
from django.urls.base import reverse

# Create your models here.
# каждый класс соответствует таблицам базы данных

class ProductManager(models.Manager):
    def update_price(self, k):
        self.get_queryset().all().update(cost = k*models.F('cost'))

    def get_queryset(self):
        return super().get_queryset().filter(cost__gt=1000) # переопределение фильтра -

class AllCatsManager(models.Manager):
    pass

class Brand(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField('Название', help_text="Здесь введите название товара", max_length=30)
    desc = models.TextField('Описание', null=True)
    cost = models.FloatField('Цена')
    slug = models.SlugField(max_length=50)
    active = models.BooleanField('Активный', default=False)
    brand = models.ForeignKey(Brand) #ключ на таблицу Brand - Brand как отдельный класс

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def cap_name(self):
        return self.name.upper()

    all_cats = AllCatsManager()
    objects = ProductManager()

    def get_absolute_url(self):
        return reverse('products:details', args=[self.slug])

# каждый класс - это новая таблица в базе


class Notebook(models.Model):
    price = models.PositiveIntegerField()
    name = models.CharField(max_length=30)

    class Meta:
        abstract = True

    def get_price(self):
        return self.price

class iBook(Notebook):
    ram = models.PositiveIntegerField
    cpu = models.CharField(max_length=20)

class IIBook(iBook):
    sensor = models.BooleanField(default=True)