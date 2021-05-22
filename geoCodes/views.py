from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import GeogInfo
import requests
import datetime
# Create your views here.
@csrf_exempt
def geoData(request):
    lat = input("Enter Latitude:->")
    lon = input("Enter Longitude:->")
    link = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=hourly,daily&units=metric&appid=08734daabf83dce36eab5788b4939a4b'.format(lat,lon)
    print("\n======================\nadding latitude and longitude into following link\n {}\n======================\n".format(link))
    response = requests.get(link)
    geodata = response.json()
    latitude = geodata["lat"]
    longitude = geodata["lon"]
    timezone = geodata["timezone"]
    current_date = datetime.datetime.fromtimestamp(float(geodata["current"]["dt"]))
    current_sunrise = datetime.datetime.fromtimestamp(float(geodata["current"]["sunrise"]))
    current_sunset = datetime.datetime.fromtimestamp(float(geodata["current"]["sunset"]))
    current_temp = geodata["current"]["temp"]

    # if request.method == 'GET':




    # dt = datetime.datetime.fromtimestamp(float(current_sunrise))
    
    return JsonResponse({"Latitude":latitude,
                        "Longitude":longitude,
                        "TimeZone": timezone,
                        "current_date":current_date,
                        "current_sunrise":current_sunrise,
                        "current_sunset":current_sunset,
                        "current_temp":current_temp
                        })
                        # ,safe = False)
    # return render(geodata["lat"])
    
    # return render(request,'geo.html',{
    #     'lat':geodata["lat"],
    #     'lon':geodata["lon"],

    # })