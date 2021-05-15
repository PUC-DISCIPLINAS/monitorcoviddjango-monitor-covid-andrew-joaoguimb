from django.contrib import admin

# Register your models here.
from .models import Covid, Country

admin.site.register(Country)
admin.site.register(Covid)
