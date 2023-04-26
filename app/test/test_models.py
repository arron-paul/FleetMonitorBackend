from datetime import datetime
from django.utils import timezone

from django.db import IntegrityError
from django.test import TestCase
from app.models import Sensor, SensorRecord, TEMPERATURE_CHOICE_CELSIUS, TEMPERATURE_CHOICE_FAHRENHEIT


class TestModel(TestCase):

    def setUp(self) -> None:
        self.date: datetime = timezone.make_aware(datetime.now(), timezone=timezone.get_current_timezone())

    def test_create_sensor(self):
        """
        Ensure can create a sensor model instance
        """
        sensor: Sensor = Sensor.objects.create(name='Generic Sensor', unit=TEMPERATURE_CHOICE_CELSIUS)
        self.assertIsInstance(sensor, Sensor)
        self.assertEqual(sensor.name, 'Generic Sensor')
        self.assertEqual(sensor.unit, TEMPERATURE_CHOICE_CELSIUS)

    def test_cannot_create_two_sensors_with_same_name(self):
        """
        Ensure two or more sensor instances cannot have the same name
        """

        # Case-sensitive
        Sensor.objects.create(name='Generic Sensor', unit=TEMPERATURE_CHOICE_CELSIUS)
        with self.assertRaises(IntegrityError):
            Sensor.objects.create(name='Generic Sensor', unit=TEMPERATURE_CHOICE_FAHRENHEIT)

    def test_create_sensor_record(self):
        """
        Ensure can create a sensor record model instance
        """
        sensor: Sensor = Sensor.objects.create(name='Generic Sensor', unit=TEMPERATURE_CHOICE_CELSIUS)
        sensor_record: SensorRecord = SensorRecord.objects.create(
            sensor=sensor,
            date=self.date,
            value=20.0)
        self.assertIsInstance(sensor_record, SensorRecord)
        self.assertIsInstance(sensor_record.sensor, Sensor)
        self.assertEqual(sensor_record.sensor.name, 'Generic Sensor')
        self.assertEqual(sensor_record.sensor.unit, TEMPERATURE_CHOICE_CELSIUS)
        self.assertEqual(sensor_record.value, 20.0)
