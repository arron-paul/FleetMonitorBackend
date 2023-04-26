from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase

from app.models import Sensor, SensorRecord, TEMPERATURE_CHOICE_CELSIUS


class TestSensorRecordViewSet(APITestCase):

    def setUp(self) -> None:
        # Create a sensor before records are added to them
        sensor_name: str = 'Main Bearing Temperature'
        sensor_unit: str = TEMPERATURE_CHOICE_CELSIUS
        self.sensor: Sensor = Sensor.objects.create(name=sensor_name, unit=sensor_unit)
        self.sensor_id = self.sensor.id

    def test_create_sensor_record(self) -> None:
        """
        Ensure ability to create a record at `/api/data` which can store
        and retrieve floating point numerical measurements from sensors.
        """
        response: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': 'Main Bearing Temperature',
                'date': '2023-04-25T17:01:05.139017Z',
                'value': 12.0
            })

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual('Main Bearing Temperature', response.json().get('sensor'))
        self.assertEqual('2023-04-25T17:01:05.139017Z', response.json().get('date'))
        self.assertEqual(12.0, response.json().get('value'))

    def test_get_sensor_record(self) -> None:
        """
        Ensure ability to retrieve information about a specific data record at `/api/data/<record_id>`
        """
        created_record: SensorRecord = SensorRecord.objects.create(
            sensor=self.sensor,
            date="2023-04-25T17:01:05.139017Z",
            value=12.0)
        response: Response = self.client.get(path=f'/api/data/{created_record.id}/', format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_list_all_sensor_records(self) -> None:
        """
        Ensure ability to list all records at `/api/data`
        """
        record_count: int = 12
        for i in range(record_count):
            SensorRecord.objects.create(
                sensor=self.sensor,
                date="2023-04-25T17:01:05.139017Z",
                value=12)
        list_sensors_response: Response = self.client.get(f'/api/data/')
        self.assertEqual(status.HTTP_200_OK, list_sensors_response.status_code)
        self.assertEqual(len(list(list_sensors_response.data)), record_count)

    def test_create_records_in_celsius_change_sensor_to_fahrenheit_ensure_record_has_correct_temperature(self):
        """
        Ensure that if a sensor changes its unit from Celsius to Fahrenheit, that it doesn't
        affect the existing record values.
        """

        # Create a sensor
        create_sensor: Response = self.client.post(
            path=f'/api/sensor/',
            format='json',
            data={
                'name': 'Custom Sensor',
                'unit': 'Celsius'
            })
        self.assertEqual(status.HTTP_201_CREATED, create_sensor.status_code)
        self.assertEqual('Celsius', create_sensor.data.get('unit'))

        # Add a record
        create_record: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': 'Custom Sensor',
                'date': '2023-04-25T17:01:05.139017Z',
                'value': 80.0
            })
        self.assertEqual(status.HTTP_201_CREATED, create_record.status_code)
        self.assertEqual(80.0, create_record.json().get('value'))

        # Modify sensor unit from Celsius to Fahrenheit
        modify_sensor: Response = self.client.patch(
            path=f'/api/sensor/1/',
            format='json',
            data={
                'unit': 'Fahrenheit'
            })
        self.assertEqual(status.HTTP_200_OK, modify_sensor.status_code)
        self.assertEqual('Fahrenheit', modify_sensor.data.get('unit'))

        # Re-check record
        lookup_record: Response = self.client.get(path=f'/api/data/?sensor=Custom Sensor')
        self.assertEqual(status.HTTP_200_OK, lookup_record.status_code)
        self.assertEqual(80.0, lookup_record.json()[0].get('value'))
