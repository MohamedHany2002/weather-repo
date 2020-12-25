



from django.urls import path
from . import views

app_name='core'

urlpatterns = [
    path('',views.home,name='home'),
    path('add_weather/',views.add_weather,name='add_weather'),
    path('delete_summary/',views.delete_summary,name='delete_summary'),
    path('summaries/',views.get_summaries,name='summaries'),

]
