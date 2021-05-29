from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.models import User
from geoCodes.models import GeogInfo
from geoCodes.views import GeogInfoViewSet,GeogInfoListView
from geoCodes.serializers import GeogInfoSerializer
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'GeogInfo',GeogInfoViewSet,basename='geog')
# router.register(r'GeogAdd',GeogInfoViewSet.geoDataAdd,basename='add')
urlpatterns = [
    path('add/',GeogInfoViewSet.geoDataAdd,name='add'),
    path('filter/',GeogInfoListView,name='filter')
    # path('', views.geoData,name='GeoData'),
    # path('get/', views.geoInfo,name='GeoInfo'),
]
