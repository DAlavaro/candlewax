# Generated by Django 4.1.7 on 2023-03-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('vendor_code', models.IntegerField()),
                ('compound', models.CharField(max_length=255)),
                ('burn_time', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('weight', models.CharField(max_length=255)),
                ('quantity_per_box', models.IntegerField()),
                ('price', models.IntegerField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('Time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('Time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
