from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from candle.views import pageNotFound
from django.urls import path, include

from candlewax import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('candle.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Обработчик для страницы 404
handler404 = pageNotFound
