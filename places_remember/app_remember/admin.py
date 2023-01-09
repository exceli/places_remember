from django.contrib import admin
from .models import Place
from django_ymap.admin import YmapAdmin


class PlaceAdmin(YmapAdmin, admin.ModelAdmin):
    list_display = ['id', 'title', 'review', 'created_at']
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Place, PlaceAdmin)

