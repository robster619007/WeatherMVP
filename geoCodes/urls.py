from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.models import User
from geoCodes.models import GeogInfo
from geoCodes.views import GeogInfoViewSet,GeogInfofilter,Geog
from geoCodes.serializers import GeogInfoSerializer
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'GeogInfo',Geog,basename='geog')
# router.register(r'save',GeogInfoViewSet,basename='save')
# router.register(r'GeogAdd',GeogInfoViewSet.geoDataAdd,basename='add')
urlpatterns = [
    path('add/',GeogInfoViewSet.geoDataAdd,name='add'),
    path('filter/',GeogInfofilter,name='filter'),
    path('',include(router.urls)),
    path('save/',GeogInfoViewSet.save,name='save')
    # path('', views.geoData,name='GeoData'),
    # path('get/', views.geoInfo,name='GeoInfo'),
]
