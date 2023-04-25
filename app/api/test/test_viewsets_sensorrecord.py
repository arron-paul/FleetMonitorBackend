from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase

from app.models import Sensor, SensorRecord, UNIT_CHOICES_CELSIUS


class TestSensorRecordViewSet(APITestCase):

    def setUp(self) -> None:
        sensor_name: str = 'Main Bearing Temperature'
        sensor_unit: str = UNIT_CHOICES_CELSIUS
        self.sensor: Sensor = Sensor.objects.create(name=sensor_name, unit=sensor_unit)
        self.sensor_id = self.sensor.id

    def test_create_sensor_record(self) -> None:

        # Spec: Create an API endpoint to store data records at /api/data/
        # which you can store and retrieve floating point numerical measurements from sensors.

        name: str = self.sensor.name
        date = "2023-04-25T17:01:05.139017Z"
        value = 12.0

        response: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': name,
                'date': date,
                'value': value
            })

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(name, response.data.get('sensor'))
        self.assertEqual(date, response.data.get('date'))
        self.assertEqual(value, response.data.get('value'))

    def test_get_sensor_record(self) -> None:

        # Spec: You should be able to retrieve information about a specific data record at /api/data/<record_id>/

        created_sensor_record: SensorRecord = SensorRecord.objects.create(
            sensor=self.sensor,
            date="2023-04-25T17:01:05.139017Z",
            value=12.0
        )

        response: Response = self.client.get(path=f'/api/data/{created_sensor_record.id}/', format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_list_all_sensor_records(self) -> None:

        # Spec: ...and a list of all of the records at `/api/data/`.

        sensor_record_count: int = 12
        for i in range(sensor_record_count):
            SensorRecord.objects.create(sensor=self.sensor, date="2023-04-25T17:01:05.139017Z", value=12)

        list_sensors_response: Response = self.client.get(f'/api/data/')
        self.assertEqual(status.HTTP_200_OK, list_sensors_response.status_code)
        self.assertEqual(len(list(list_sensors_response.data)), sensor_record_count)
