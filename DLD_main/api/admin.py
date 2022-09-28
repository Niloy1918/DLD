from django.contrib import admin
from api.models import DeviceInformation

class DeviceInformationAdmin(admin.ModelAdmin):
    list_display= ["deviceId","inflow","outflow","inPressure","outPressure","temperature","differential","created_at","updated_at"]

admin.site.register(DeviceInformation,DeviceInformationAdmin)