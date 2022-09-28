from django.contrib import admin
from django.urls import path, include
from api.views import DeviceInformationViewset


urlpatterns = [
    path('deviceinformation', DeviceInformationViewset.as_view()),
]
