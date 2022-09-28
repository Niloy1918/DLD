from dataclasses import fields
from rest_framework import serializers
from api.models import DeviceInformation

class DeviceInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInformation
        fields = ["deviceId","inflow","outflow","inPressure","outPressure","temperature","differential","created_at","updated_at"]    