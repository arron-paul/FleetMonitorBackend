from rest_framework.test import APITestCase

from app.api.serializers import SensorSerializer, SensorRecordSerializer
from app.models import Sensor, SensorRecord, TEMPERATURE_CHOICE_CELSIUS


class TestSensorViewSet(APITestCase):

    def test_sensor_serializer_with_valid_data(self) -> None:
        """
        Ensure sensor serializer can parse valid data
        """
        valid_inputs: list = [
            ('Sensor 1', 'Celsius'),
            ('Sensor 2', 'Fahrenheit')
        ]
        for valid_input in valid_inputs:
            data: dict = {'name': valid_input[0], 'unit': valid_input[1]}
            sensor_serializer: SensorSerializer = SensorSerializer(data=data)
            self.assertTrue(sensor_serializer.is_valid())
            sensor: Sensor = sensor_serializer.save()
            self.assertIsInstance(sensor, Sensor)

    def test_sensor_serializer_with_invalid_data(self) -> None:
        """
        Ensure sensor serializer cannot parse invalid data
        """
        invalid_inputs: list = [
            ('Sensor 1', '1'),
            ('Sensor 2', 'False'),
            ('Sensor 3', 'Degrees Celsius')
        ]
        for invalid_input in invalid_inputs:
            data: dict = {'name': invalid_input[0], 'unit': invalid_input[1]}
            sensor_serializer: SensorSerializer = SensorSerializer(data=data)
            self.assertFalse(sensor_serializer.is_valid())
            with self.assertRaises(AssertionError):
                sensor: Sensor = sensor_serializer.save()

    def test_sensor_record_serializer_with_valid_data(self) -> None:
        """
        Ensure sensor record serializer can parse valid data
        """
        Sensor.objects.create(name='Sensor 1', unit=TEMPERATURE_CHOICE_CELSIUS)
        valid_inputs: list = [
            ('Sensor 1', '2023-04-25T17:01:05.139017Z', 12.0),
            ('Sensor 1', '2023-04-25T17:01:05.139017Z', 5000.0),
            ('Sensor 1', '2023-04-25T17:01:05.139017Z', -5000.0),
        ]
        for valid_input in valid_inputs:
            data: dict = {'sensor': valid_input[0], 'date': valid_input[1], 'value': valid_input[2]}
            sensor_record_serializer: SensorRecordSerializer = SensorRecordSerializer(data=data)
            self.assertTrue(sensor_record_serializer.is_valid())
            record: SensorRecord = sensor_record_serializer.save()
            self.assertIsInstance(record, SensorRecord)

    def test_sensor_record_serializer_with_invalid_data(self) -> None:
        """
        Ensure sensor record serializer cannot parse invalid data
        """
        invalid_inputs: list = [
            ('Sensor 1', '', 12.0),
            ('', '2023-04-25T17:01:05.139017Z', 5000.0),
            ('Sensor 1', 5000.0, '2023-04-25T17:01:05.139017Z'),
            (None, None, None)
        ]
        for invalid_input in invalid_inputs:
            data: dict = {'sensor': invalid_input[0], 'date': invalid_input[1], 'value': invalid_input[2]}
            sensor_record_serializer: SensorRecordSerializer = SensorRecordSerializer(data=data)
            self.assertFalse(sensor_record_serializer.is_valid())
            with self.assertRaises(AssertionError):
                sensor_record: SensorRecord = sensor_record_serializer.save()
