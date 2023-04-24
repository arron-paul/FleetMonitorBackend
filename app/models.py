from django.db import models

from app.units import UNIT_CHOICES


class Sensor(models.Model):
    """
    A Sensor that is attached to a Wind Turbine
    """
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    unit = models.SmallIntegerField(choices=UNIT_CHOICES)


class SensorRecord(models.Model):
    """
    A recorded value of a Sensor at a specific time
    """
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    value = models.FloatField()
