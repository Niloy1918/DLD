from django.contrib import admin
from api.models import DeviceInformation

class DeviceInformationAdmin(admin.ModelAdmin):
    list_display= ["deviceId","deviceName","inflow","outflow","inPressure","outPressure","temperature","differential","uploadDate","created_at","updated_at"]

admin.site.register(DeviceInformation,DeviceInformationAdmin)

# class StatusListAdmin(admin.ModelAdmin):
#     list_display = ["deviceName","createdAt","time","status"]

# admin.site.register(Statuslist,StatusListAdmin)