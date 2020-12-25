from django.contrib import admin
from .models import Weather,Summary
import json
# Register your models here.


from django.contrib import admin

from . import models

class AdminSummary(admin.ModelAdmin):
    model = Summary
    actions = ['delete_model']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            list_ids = obj.get_weather_ids()
            jsonDec = json.decoder.JSONDecoder()
            weather_ids = jsonDec.decode(list_ids)
            weather_objs = Weather.objects.filter(id__in=weather_ids).delete()
        queryset.delete()

    def delete_model(self, request, obj):
        print("hello")
        list_ids = obj.get_weather_ids()
        jsonDec = json.decoder.JSONDecoder()
        weather_ids = jsonDec.decode(list_ids)
        weather_objs = Weather.objects.filter(id__in=weather_ids).delete()
        obj.delete()
admin.site.register(Summary, AdminSummary)

admin.site.register(Weather)
