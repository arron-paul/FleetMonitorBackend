from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase

from app.models import Sensor, TEMPERATURE_CHOICE_FAHRENHEIT, TEMPERATURE_CHOICE_CELSIUS


class TestSensorViewSet(APITestCase):

    def test_create_sensor(self) -> None:
        """
        Ensure ability to create a model at `/api/sensor/` to represent a sensor.
        The payload should look like {"name": "Main Bearing Temperature", "unit": "Celsius"}
        """

        response: Response = self.client.post(
            path=f'/api/sensor/',
            format='json',
            data={
                'name': 'Main Bearing Temperature',
                'unit': 'Celsius'
            })

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual('Main Bearing Temperature', response.data.get('name'))
        self.assertEqual('Celsius', response.data.get('unit'))

    def test_unique_sensor_name(self) -> None:
        """
        Ensure sensor names are unique
        """

        payload: dict = {'name': 'Main Bearing Temperature', 'unit': 'Celsius'}

        first_response: Response = self.client.post(
            path=f'/api/sensor/', format='json', data=payload)
        self.assertEqual(status.HTTP_201_CREATED, first_response.status_code)

        second_response: Response = self.client.post(
            path=f'/api/sensor/', format='json', data=payload)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, second_response.status_code)

    def test_get_sensor(self) -> None:
        """
        Ensure ability to retrieve information about a specific sensor at `/api/sensor/<sensor_id>/`
        """

        created_sensor: Sensor = Sensor.objects.create(
            name='Main Bearing Temperature',
            unit=TEMPERATURE_CHOICE_FAHRENHEIT
        )

        response: Response = self.client.get(f'/api/sensor/{created_sensor.id}/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.data.get('name'), 'Main Bearing Temperature')
        self.assertEqual(response.data.get('unit'), 'Fahrenheit')

    def test_list_all_sensors(self) -> None:
        """
        Ensure ability to list all sensors at `/api/sensor`
        """

        sensor_count: int = 12
        for i in range(sensor_count):
            Sensor.objects.create(
                name=f'Main Bearing Temperature {i}',
                unit=TEMPERATURE_CHOICE_CELSIUS)

        list_sensors_response: Response = self.client.get(f'/api/sensor/')
        self.assertEqual(status.HTTP_200_OK, list_sensors_response.status_code)
        self.assertEqual(len(list(list_sensors_response.data)), sensor_count)
