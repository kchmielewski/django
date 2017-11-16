
from django.contrib import admin

from .models import Film, Type, Director, Place
from rent.models import Rent
# Register your models here.
class RentAdmin(admin.ModelAdmin):
    search_fields = ['who_rent', 'what_rent']
    ordering = ['who_rent', 'what_rent','when_rent','returned']
    list_display = ['who_rent', 'what_rent','when_rent','returned']

class FilmAdmin(admin.ModelAdmin):
    search_fields = ['title','director','type','production_date','price']
    ordering = ['title']
    list_display = ['title','director','type','production_date','price']

class TypeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']
    list_display = ['name']

class DirectorAdmin(admin.ModelAdmin):
    search_fields = ['name','last_name']
    ordering = ['last_name']
    list_display = ['name','last_name']

class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['country']
    ordering = ['country']
    list_display = ['country']

admin.site.register(Film, FilmAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Rent, RentAdmin)