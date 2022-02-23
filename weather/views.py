from django.shortcuts import render
import requests
from .models import *
from .form import *


def index(request):
    appid = '572b22c6ff1223ccbe43f87d7bba4c30'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    cities = City.objects.all()

    all_cities = []

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
        }

        all_cities.append(city_info)

    context = {
        "all_info": all_cities,
        "form": form
    }

    return render(request, 'weather/index.html', context)
