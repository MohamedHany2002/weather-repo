

from django.shortcuts import render,redirect,get_object_or_404
from .forms import WeatherForm
from .models import Weather,Summary
from django.db.models import Avg
import json
# Create your views here.




def add_weather(request):
    if request.method=='POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            temp = request.POST.get('temp')
            hum = request.POST.get('hum')
            Weather.objects.create(temp=temp,hum=hum)
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
            return redirect('core:home')
        else:
            return render(request,"add_weather.html",{'form':form})
    else:
        form = WeatherForm()
    return render(request,"add_weather.html",{'form':form})


def home(request):
    objs=Weather.objects.order_by('-created')
    return render(request,"home.html",{'objs':objs})


def delete_summary(request,id):
    summary = get_object_or_404(Summary,id=id)
    list_ids = summary.get_weather_ids()
    jsonDec = json.decoder.JSONDecoder()
    weather_ids = jsonDec.decode(list_ids)
    weather_objs = Weather.objects.filter(id__in=weather_ids).delete()
    summary.delete()
    return redirect('core:home')

def get_summaries(request):
    objs=Summary.objects.all()
    return render(request,"summary.html",{'objs':objs})



