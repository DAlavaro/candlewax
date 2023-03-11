from django.db import models
from django.urls import reverse


class Candle(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    vendor_code = models.IntegerField()
    compound = models.CharField(max_length=255)
    burn_time = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    quantity_per_box = models.IntegerField()
    price = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    Time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Menu(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    Time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Пункты верхнего меню'
        verbose_name_plural = 'Пункты верхнего меню'

