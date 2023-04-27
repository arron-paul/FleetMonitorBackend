from django.db import models

# Possible choices for Sensor temperature `unit`
TEMPERATURE_CHOICE_CELSIUS = 0
TEMPERATURE_CHOICE_FAHRENHEIT = 1
TEMPERATURE_CHOICES = (
    (TEMPERATURE_CHOICE_CELSIUS, 'Celsius'),
    (TEMPERATURE_CHOICE_FAHRENHEIT, 'Fahrenheit')
)


class Sensor(models.Model):
    """
    A Sensor that is attached to a Wind Turbine
    """
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    unit = models.PositiveSmallIntegerField(choices=TEMPERATURE_CHOICES)


class SensorRecord(models.Model):
    """
    A recorded value of a Sensor at a specific time
    """
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    value = models.FloatField()
