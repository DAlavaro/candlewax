from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *


# Функция базового шаблона
posts = [
    {'title': 'Инфо', 'url_name': 'info'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Доставка', 'url_name': 'delivery'},
    {'title': 'Отзывы', 'url_name': 'reviews'},
]


# Функция главной страницы сайта
def index(request):
    context = {'posts': posts,
               'title': 'Восковая свеча - свечи из 100% пчелиного воска'}
    return render(request, 'candle/index.html', context=context)


# Функция страницы информации о продукте
def info(request):
    context = {'posts': posts,
               'title': 'Восковая свеча - свечи из 100% пчелиного воска'}
    return render(request, 'candle/info.html', context=context)


# Функция страницы информации о фирме
def about(request):
    context = {'posts': posts,
               'title': 'Восковая свеча - свечи из 100% пчелиного воска'}
    return render(request, 'candle/about.html', context=context)


# Функция страницы о доставке
def delivery(request):
    context = {'posts': posts,
               'title': 'Восковая свеча - свечи из 100% пчелиного воска'}
    return render(request, 'candle/delivery.html', context=context)


# Страница отзывов
def reviews(request):
    context = {'posts': posts,
               'title': 'Восковая свеча - свечи из 100% пчелиного воска'}
    return render(request, 'candle/reviews.html', context=context)


# функция для обработчика 404
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')