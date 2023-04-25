from django.db import models

# Possible choices for Sensor temperature `unit`
UNIT_CHOICES_CELSIUS = 1
UNIT_CHOICES_FAHRENHEIT = 2
UNIT_CHOICES = (
    (UNIT_CHOICES_CELSIUS, 'Celsius'),
    (UNIT_CHOICES_FAHRENHEIT, 'Fahrenheit')
)


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
    date = models.DateTimeField()
    value = models.FloatField()
