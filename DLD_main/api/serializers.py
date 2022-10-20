from dataclasses import fields
from operator import mod
from rest_framework import serializers
from api.models import DeviceInformation,Statuslist,InformationLog

class DeviceInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInformation
        fields = ["id","deviceId","inflow","outflow","inPressure","outPressure","temperature","differential","created_at","updated_at"]

class StatuslistSerializer(serializers.ModelSerializer):
    deviceId=serializers.SerializerMethodField()
    class Meta:
        model = Statuslist
        fields = ["deviceId","createdAt","time","status"]
    def get_deviceId(self,Statuslist):
        return Statuslist.deviceId.deviceId

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationLog
        fields = ["deviceId","inflow","outflow","inPressure","outPressure","temperature","differential","created_at","updated_at"]
    
