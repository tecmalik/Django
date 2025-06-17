from django.contrib import admin
from . import models
from .models import Language


# Register your models here.

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'language', 'isbn']
    list_filter = ['isbn']
    search_fields = ['title']
    list_per_page = 10

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Language)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']


# admin.site.register(models.Book)
# admin.site.register(models.Language)
# admin.site.register(models.Genre)
# admin.site.register(models.Language)