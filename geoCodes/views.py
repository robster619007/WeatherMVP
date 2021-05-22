from django.shortcuts import render
from django.http import JsonResponse
import requests
import datetime
# Create your views here.
def geoData(request):
    response = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=33.441792&lon=-94.037689&exclude=hourly,daily&appid=08734daabf83dce36eab5788b4939a4b')
    geodata = response.json()
    geotime = geodata["current"]["sunrise"]

    dt = datetime.datetime.fromtimestamp(float(geotime))
    
    return JsonResponse({"Latitude":geodata["lat"],
                        "Longitude":geodata["lon"],
                        "TimeZone":geodata["timezone"],
                        "Current Sunset":dt})
                        # ,safe = False)
    # return render(geodata["lat"])
    
    # return render(request,'geo.html',{
    #     'lat':geodata["lat"],
    #     'lon':geodata["lon"],

    # })