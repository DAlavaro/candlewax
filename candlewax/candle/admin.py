from django.contrib import admin

from .models import Menu, Candle

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Menu, MenuAdmin)
admin.site.register(Candle)


