from django.contrib import admin
from django.urls import path, include
from api.views import DeviceInformationViewset


urlpatterns = [
    path('deviceinformation/', DeviceInformationViewset.as_view()),
    # path('deviceinformation/<int:id>/',DeviceInformationViewset.as_view()),
    # path('statuslist', StatusListViewset.as_view()),
]
