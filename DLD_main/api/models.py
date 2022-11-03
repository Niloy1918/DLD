from django.db import models

class DeviceInformation(models.Model):
    deviceId = models.CharField(max_length=1000,blank=True)
    deviceName = models.CharField(max_length=1000,blank=True)
    inflow = models.FloatField(max_length=1000,blank=True)
    outflow = models.FloatField(max_length=1000,blank=True)
    inPressure = models.FloatField(max_length=1000,blank=True)
    outPressure = models.FloatField(max_length=1000,blank=True)
    temperature = models.FloatField(max_length=1000,blank=True)
    differential = models.FloatField(max_length=1000,blank=True)
    offset = models.FloatField(blank = True)
    uploadDate = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Device Informations"

    def __str__(self):
        return self.deviceId

# class Statuslist(models.Model):
#     deviceName = models.ForeignKey(DeviceInformation,on_delete=models.CASCADE)
#     createdAt = models.DateField(auto_now_add=True)
#     time = models.TimeField(auto_now_add=True)
#     status = models.CharField(max_length=1000,blank=True) 

#     class Meta:
#         verbose_name_plural = "Statuslist"

#     def __str__(self):
#         return str(self.deviceName.deviceName)


# class InformationLog(models.Model):
#     deviceId = models.CharField(max_length=1000,blank=True) 
#     inflow = models.FloatField(max_length=1000,blank=True)
#     outflow = models.FloatField(max_length=1000,blank=True)
#     inPressure = models.FloatField(max_length=1000,blank=True)
#     outPressure = models.FloatField(max_length=1000,blank=True)
#     temperature = models.FloatField(max_length=1000,blank=True)
#     differential = models.FloatField(max_length=1000,blank=True)
#     offset = models.FloatField(blank = True)
#     database_created_at = models.DateTimeField(auto_now_add=True)
#     database_updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name_plural = "Information Log"

#     def __str__(self):
#         return self.deviceId    