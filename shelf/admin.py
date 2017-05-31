
from django.contrib import admin

from .models import Film, Type, Director
# Register your models here.

class FilmAdmin(admin.ModelAdmin):
    search_fields = ['title','director','type','production_date']
    ordering = ['title']
    list_display = ['title','director','type','production_date']

class TypeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']
    list_display = ['name']

class DirectorAdmin(admin.ModelAdmin):
    search_fields = ['name','last_name']
    ordering = ['last_name']
    list_display = ['name','last_name']

admin.site.register(Film, FilmAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Director, DirectorAdmin)