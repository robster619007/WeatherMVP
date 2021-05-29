from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import GeogInfo
from .serializers import GeogInfoSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import datetime

class GeogInfoViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = GeogInfo.objects.all()
        serializer = GeogInfoSerializer(queryset,many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk=None):
        queryset = GeogInfo.objects.all()
        geog = get_object_or_404(queryset, pk=pk)
        serializer = GeogInfoSerializer(geog)
        return Response(serializer.data)  
    def geoDataAdd(self,request):
        lat = input("Enter Latitude:->")
        lon = input("Enter Longitude:->")
        link = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=hourly,daily&units=metric&appid=08734daabf83dce36eab5788b4939a4b'.format(lat,lon)
        print("\n======================\nadding latitude and longitude into following link\n {}\n======================\n".format(link))
        response = requests.get(link)
        g = GeogInfo()
        geodata = response.json()
        g.latitude = geodata["lat"]
        g.longitude = geodata["lon"]
        g.timezone = geodata["timezone"]
        g.current_date = datetime.datetime.fromtimestamp(float(geodata["current"]["dt"]))
        g.current_sunrise = datetime.datetime.fromtimestamp(float(geodata["current"]["sunrise"]))
        g.current_sunset = datetime.datetime.fromtimestamp(float(geodata["current"]["sunset"]))
        g.current_temp = geodata["current"]["temp"]

    # return JsonResponse({"Latitude":g.latitude,
    #                     "Longitude":g.longitude,
    #                     "TimeZone": g.timezone,
    #                     "current_date":g.current_date,
    #                     "current_sunrise":g.current_sunrise,
    #                     "current_sunset":g.current_sunset,
    #                     "current_temp":g.current_temp,
    #                     "Saved??":"yes"
    #                     })
