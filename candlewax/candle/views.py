from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Функция главной страницы сайта
def index(request):
    return render(request, 'candle/index.html', {'title': 'Восковая свеча - свечи из 100% пчелиного воска'})


# Функция страницы информации о продукте
def info(request):
    return render(request, 'candle/info.html', {'title': 'Почему восковая свеча, а не парафиновая?'})


# Функция страницы информации о фирме
def about(request):
    return HttpResponse('Страница информации о фирме')


# Функция страницы о доставке
def delivery(request):
    return HttpResponse('Оплата и доставка')


# Страница отзывов
def reviews(request, rev):
    return HttpResponse(f'<h1>Здесь Вы можете оставить свои отзывы и комментарии номер {rev}</h1>')


# функция для обработчика 404
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')