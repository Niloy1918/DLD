from django.shortcuts import render,get_object_or_404
from api.models import DeviceInformation
from api.serializers import DeviceInformationSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
import json
from fractions import Fraction
from django.http import JsonResponse

# @csrf_exempt
# @method_decorator(csrf_exempt, name='dispatch')
class DeviceInformationViewset(APIView):
    queryset = DeviceInformation.objects.all()
    serializer_class = DeviceInformationSerializer
    renderer_classes = [JSONRenderer]
    # print(queryset)
    def get_queryset(self):
        deviceInfromation = DeviceInformation.objects.all()
        return deviceInfromation

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                deviceInformation = deviceInformation.objects.get(id=id)
                serializer = DeviceInformationSerializer(deviceInformation)
        except:
            deviceInformation = self.get_queryset()
            serializer = DeviceInformationSerializer(deviceInformation,many=True)

        return JsonResponse({"data":serializer.data})


    def post(self, request, *args, **kwargs):
        deviceInformationData =  json.loads(request.body.decode('UTF-8'))
        # print (deviceInformationData)
        # return Response(deviceInformationData['inflow'])
        # inlet_flow_sensor_data = float(deviceInformationData['inflow'])
        # outlet_flow_sensor_data = float(deviceInformationData['outflow'])
        # inlet_pressure_sensor_data = Fraction(deviceInformationData['inPressure'])
        # outlet_pressure_sensor_data = Fraction(deviceInformationData['outPressure'])
        offset1 = 0.483
        offset2 = 0.339
        # ratio = Fraction(inlet_pressure_sensor_data, outlet_pressure_sensor_data).limit_denominator()
        # differential = (ratio.numerator/10**6)/(ratio.denominator / 10**6)
        # print(deviceInformationData)
        # inflow_value = (inlet_flow_sensor_data * (60/7.5))
        # print(inflow_value)
        # outflow_value = (outlet_flow_sensor_data * (60/7.5))
        # inPressure_value = (inlet_pressure_sensor_data - offset1) * 250 
        # outPressure_value = (outlet_pressure_sensor_data - offset2) * 250
        # temperature = 89

        newDeviceinformation = DeviceInformation.objects.get()
        newDeviceinformation.deviceId = deviceInformationData['deviceId']
        newDeviceinformation.inflow = deviceInformationData['inflow']
        newDeviceinformation.outflow = deviceInformationData['outflow']
        newDeviceinformation.inPressure = deviceInformationData['inPressure']
        newDeviceinformation.outPressure = deviceInformationData['outPressure']
        newDeviceinformation.temperature = deviceInformationData['temperature']
        newDeviceinformation.differential = deviceInformationData['differential']
        newDeviceinformation.offset = 0
        
        print(newDeviceinformation)
        newDeviceinformation.save()

        serializer = DeviceInformationSerializer(newDeviceinformation)

        return Response(serializer.data)        
    
    # @csrf_exempt
    # def post(self, request, *args, **kwargs):
    #     deviceInformationData =  json.loads(request.body.decode('UTF-8'))
    #     # print (deviceInformationData)
    #     # return Response(deviceInformationData['inflow'])
    #     inlet_flow_sensor_data = float(deviceInformationData['inflow'])
    #     outlet_flow_sensor_data = float(deviceInformationData['outflow'])
    #     inlet_pressure_sensor_data = Fraction(deviceInformationData['inPressure'])
    #     outlet_pressure_sensor_data = Fraction(deviceInformationData['outPressure'])
    #     offset1 = 0.483
    #     offset2 = 0.339
    #     ratio = Fraction(inlet_pressure_sensor_data, outlet_pressure_sensor_data).limit_denominator()
    #     differential = (ratio.numerator/10**6)/(ratio.denominator / 10**6)
    #     # print(deviceInformationData)
    #     inflow_value = (inlet_flow_sensor_data * (60/7.5))
    #     print(inflow_value)
    #     outflow_value = (outlet_flow_sensor_data * (60/7.5))
    #     inPressure_value = (inlet_pressure_sensor_data - offset1) * 250 
    #     outPressure_value = (outlet_pressure_sensor_data - offset2) * 250
    #     temperature = 89

    #     newDeviceinformation = DeviceInformation.objects.get()
    #     newDeviceinformation.deviceId = deviceInformationData['deviceId']
    #     newDeviceinformation.inflow = inflow_value
    #     newDeviceinformation.outflow = outflow_value
    #     newDeviceinformation.inPressure = inPressure_value
    #     newDeviceinformation.outPressure = outPressure_value
    #     newDeviceinformation.temperature = temperature
    #     newDeviceinformation.differential = differential
    #     newDeviceinformation.offset = 0
        
    #     print(newDeviceinformation)
    #     newDeviceinformation.save()

    #     serializer = DeviceInformationSerializer(newDeviceinformation)

    #     return Response(serializer.data)

# class StatusListViewset(APIView):
#     queryset = Statuslist.objects.all()
#     serializer_class = StatuslistSerializer
#     renderer_classes = [JSONRenderer]    

#     def get_queryset(self):
#         statusList = Statuslist.objects.all()
#         # for deviceIds in statusList:
#         #     deviceId = deviceIds.deviceId
#         #     print(deviceId)
#         return statusList

#     def get(self, request, *args, **kwargs):
#         try:
#             deviceId = request.query_params["id"]
#             if id != None:
#                 statusList = statusList.objects.get(deviceId=deviceId)
#                 serializer = StatuslistSerializer(statusList)
#         except:
#             statusList = self.get_queryset()
#             serializer = StatuslistSerializer(statusList,many=True)

#         return JsonResponse({"data":serializer.data})


    # def put(self, request, *args, **kwargs):
    #     deviceInformationObject = DeviceInformation.objects.get(deviceId=request.POST.get("deviceId"))

    #     deviceInformationData = request.data

    #     inlet_flow_sensor_data = float(deviceInformationData ("inlet_flow_sensor_data"))
    #     outlet_flow_sensor_data = float(deviceInformationData("outlet_flow_sensor_data"))
    #     inlet_pressure_sensor_data = float(deviceInformationData("inlet_pressure_sensor_data"))
    #     outlet_pressure_sensor_data = float(deviceInformationData("outlet_pressure_sensor_data"))
    #     offset = float(deviceInformationData("OffSet"))

    #     inflow_value = (inlet_flow_sensor_data * (60/7.5))
    #     outflow_value = (outlet_flow_sensor_data * (60/7.5))
    #     inPressure_value = (inlet_pressure_sensor_data - offset) * 250 
    #     outPressure_value = (outlet_pressure_sensor_data - offset) * 250


    #     deviceInformationObject.deviceId = deviceInformationData["deviceId"]
    #     deviceInformationObject.inflow = inflow_value
    #     deviceInformationObject.outflow = outflow_value
    #     deviceInformationObject.inPressure = inPressure_value
    #     deviceInformationObject.outPressure = outPressure_value
    #     deviceInformationObject.temperature = deviceInformationData["temperature"]
    #     deviceInformationData.differential = deviceInformationData["differential"]
    #     deviceInformationData.offset = offset

    #     deviceInformationObject.save()
        
    #     serializer = DeviceInformationSerializer(deviceInformationObject)
    #     return Response(serializer.data)






