from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Registration)
admin.site.register(CountryMaster)
admin.site.register(StateMaster)
admin.site.register(CityMaster)
admin.site.register(GenderMaster)
admin.site.register(SendMessage)
admin.site.register(BloodGroupMaster)
admin.site.register(UploadFile)