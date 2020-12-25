from django.db import models

# Create your models here.


class Weather(models.Model):
    temp = models.FloatField()
    hum = models.FloatField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True,blank=True)

    # def __str__(self):
    #     return self.temp + self.hum


class Summary(models.Model):
    avg_temp = models.FloatField()
    avg_hum = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True,blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    list_ids = models.TextField(max_length=20)

    def get_weather_ids(self):
        return self.list_ids

    # def __str__(self):
    #     return self.avg_hum+self.avg_temp