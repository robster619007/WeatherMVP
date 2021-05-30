from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import GeogInfo
from .serializers import GeogInfoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import django_filters.rest_framework
# from weather.permissions import IsAdminOrIsSelf
from rest_framework.decorators import action
import requests
import datetime
# http://127.0.0.1:8000/wapi/filter
class GeogInfoListView(viewsets.ReadOnlyModelViewSet):
    queryset = GeogInfo.objects.all()
    serializer_class = GeogInfoSerializer
    serializer = GeogInfoSerializer(queryset,many =True)
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['latitude','longitude','timezone','current_temp']

# API to be used
class GeogInfoViewSet(viewsets.ViewSet):
    # http://127.0.0.1:8000/Geog/
    def list(self,request):
        queryset = GeogInfo.objects.all()
        serializer = GeogInfoSerializer(queryset,many=True)
        serializer_class = GeogInfoSerializer
        filter_backends = [DjangoFilterBackend]
        # filterset_fields = ['latitude','longitude','timezone','current_temp']
        return Response(serializer.data)
    # http://127.0.0.1:8000/Geog/<pk> in this case its 1,2,3
    def retrieve(self,request,pk=None):
        queryset = GeogInfo.objects.all()
        geog = get_object_or_404(queryset, pk=pk)
        serializer = GeogInfoSerializer(geog)
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['latitude','longitude','timezone','current_temp']
        return Response(serializer.data)
    # Use this function to add according to the longitude and latitude. As soon as the wapi/add url is executed
    # the terminal should show which latitude and longitude to enter. By entering the values the data from the 
    # open api according to the longitude and latitude will be used to save the data in the model.
    # api http://127.0.0.1:8000/wapi/add
    def geoDataAdd(request):
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
        g.save()
        return JsonResponse({"Latitude":g.latitude,
                            "Longitude":g.longitude,
                            "TimeZone": g.timezone,
                            "current_date":g.current_date,
                            "current_sunrise":g.current_sunrise,
                            "current_sunset":g.current_sunset,
                            "current_temp":g.current_temp,
                            "Saved??":"yes"
                            })
