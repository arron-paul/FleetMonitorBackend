from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase

from app.models import Sensor, UNIT_CHOICES_CELSIUS, UNIT_CHOICES_FAHRENHEIT

# todo: APITestCases need to know about the base path
BASE_PATH = 'http://127.0.0.1:8000'


class TestSensorViewSet(APITestCase):

    def test_create_sensor(self) -> None:

        # Spec: Create a model and API (at /api/sensor/) to represent a "sensor".
        # You should be able to create sensors at the end point with a payload like
        # '{"name": "Main Bearing Temperature", "unit": "Celsius"}'

        sensor_name: str = 'Main Bearing Temperature'
        sensor_unit: str = 'Celsius'

        response: Response = self.client.post(
            path=f'{BASE_PATH}/api/sensor/',
            format='json',
            data={
                'name': sensor_name,
                'unit': sensor_unit
            })

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(sensor_name, response.data.get('name'))
        self.assertEqual(sensor_unit, response.data.get('unit'))

    def test_unique_sensor_name(self) -> None:

        # Spec: Sensor names should be unique.

        sensor_name: str = 'Main Bearing Temperature'
        sensor_unit: str = 'Celsius'

        payload: dict = {
            'name': sensor_name,
            'unit': sensor_unit
        }

        first_response: Response = self.client.post(path=f'{BASE_PATH}/api/sensor/', format='json', data=payload)
        self.assertEqual(status.HTTP_201_CREATED, first_response.status_code)

        second_response: Response = self.client.post(path=f'{BASE_PATH}/api/sensor/', format='json', data=payload)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, second_response.status_code)

    def test_get_sensor(self) -> None:

        # Spec: You should be able to retrieve information about a specific sensor at /api/sensor/<sensor_id>/

        sensor_name: str = 'Main Bearing Temperature'
        sensor_unit: int = UNIT_CHOICES_FAHRENHEIT

        created_sensor: Sensor = Sensor.objects.create(name=sensor_name, unit=sensor_unit)

        response: Response = self.client.get(f'{BASE_PATH}/api/sensor/{created_sensor.id}/')

        expected_name: str = response.data.get('name')
        expected_unit: str = response.data.get('unit')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_name, sensor_name)
        self.assertEqual(expected_unit, 'Fahrenheit')

    def test_list_all_sensors(self) -> None:

        # Spec: ...and a list of all of the sensors at /api/sensor/

        sensor_count: int = 12
        for i in range(sensor_count):
            sensor_name: str = f'Main Bearing Temperature {i}'
            sensor_unit: str = UNIT_CHOICES_CELSIUS
            Sensor.objects.create(name=sensor_name, unit=sensor_unit)

        list_sensors_response: Response = self.client.get(f'{BASE_PATH}/api/sensor/')
        self.assertEqual(status.HTTP_200_OK, list_sensors_response.status_code)
        self.assertEqual(len(list(list_sensors_response.data)), sensor_count)
