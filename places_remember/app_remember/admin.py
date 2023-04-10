from django.contrib import admin
from .models import Place, Images
from django_ymap.admin import YmapAdmin



class PlaceImages(admin.TabularInline):
    model = Images


class PlaceAdmin(YmapAdmin, admin.ModelAdmin):
    list_display = ['id', 'title', 'review', 'created_at']
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    inlines = (
        PlaceImages,
    )


admin.site.register(Place, PlaceAdmin)

