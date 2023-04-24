from django.contrib import admin

from app.models import Sensor, SensorRecord

admin.site.register(Sensor)
admin.site.register(SensorRecord)
