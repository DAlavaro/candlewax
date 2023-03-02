from django.db import models

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
