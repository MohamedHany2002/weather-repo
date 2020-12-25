from django.db import models

# Create your models here.


class Weather(models.Model):
    temp = models.FloatField()
    hum = models.FloatField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True,blank=True)

    def save(self,*args,**kwargs):
        if Weather.objects.count()%10==0:
            count_rest = Weather.objects.count()-10
            count = Weather.objects.count()
            weather_objs = Weather.objects.all()[count_rest-1:count]
            temp_avg = weather_objs.aggregate(AVG('temp'))
            hum_avg = weather_objs.aggregate(AVG('hum'))
            start_date = weather_objs.first().created
            end_date = weather_objs.last().created
            ids = Weather.objects.values_list('id',flat=True)
            weather_ids=json.dumps(ids)
            Summary.objects.create(avg_temp=temp_avg,avg_hum=hum_avg,start_date=start_date,end_date=end_date,list_ids=weather_ids)
        super().save(*args,**kwargs)

    # def __str__(self):
    #     return self.temp + self.hum


class Summary(models.Model):
    avg_temp = models.FloatField()
    avg_hum = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True,blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    list_ids = models.TextField(max_length=20,blank=True,null=True)

    def get_weather_ids(self):
        return self.list_ids

    # def __str__(self):
    #     return self.avg_hum+self.avg_temp

    # def post_delete  customized in django admin 