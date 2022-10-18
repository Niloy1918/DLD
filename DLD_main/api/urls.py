from django.contrib import admin
from django.urls import path, include
from api.views import DeviceInformationViewset,StatusListViewset


urlpatterns = [
    path('deviceinformation', DeviceInformationViewset.as_view()),
    path('statuslist', StatusListViewset.as_view()),
]
