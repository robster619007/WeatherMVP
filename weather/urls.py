"""weather URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from geoCodes.models import GeogInfo
from django.core.paginator import Paginator
from geoCodes.views import GeogInfoViewSet
from geoCodes.serializers import GeogInfoSerializer
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
import csv

class Geog(viewsets.ModelViewSet):
    queryset = GeogInfo.objects.all()
    serializer_class = GeogInfoSerializer
    # pagination_class = LargeResultsSetPagination
# Routers provide an easy way of automatically determining the URL conf.
class SaveGeogInfo(viewsets.ViewSet):
    def save(request):
        response = HttpResponse(content_type = 'text/csv')
        response['Content-Disposition'] = 'attachment; filename="GeogInfo.csv"'
        queryset = GeogInfo.objects.all()
        serializer_class = GeogInfoSerializer
        writer = csv.writer(response)
        for g in queryset:
            writer.writerow([g.latitude,g.longitude,g.timezone,g.current_date,g.current_sunrise,g.current_sunset,g.current_temp])
        return (response)
router = DefaultRouter()
router.register(r'Geog',GeogInfoViewSet,basename='geog')
router.register(r'pagination',Geog,basename='page')
router.register(r'save',SaveGeogInfo,basename='save')
# router.register(r'weatherapi', geoData)

urlpatterns = [
    path('admin/', admin.site.urls),#username:admin password:admin
    path('save/', SaveGeogInfo.save,name='save'),
    path('wapi/',include('geoCodes.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
