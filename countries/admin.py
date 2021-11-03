from django.contrib import admin
from .models import Continent, Country

class ContinentAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Continent, ContinentAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'continent']
    list_per_page = 20
admin.site.register(Country, CountryAdmin)