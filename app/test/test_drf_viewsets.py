from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase

from app.models import Sensor

# todo: APITestCases need to know about the base path
BASE_PATH = "http://127.0.0.1:8000"


class TestSensorViewSet(APITestCase):

    def test_create_sensor(self) -> None:

        payload: dict = {
            "name": "Test Sensor 1",
            "unit": "Celsius"
        }
        response: Response = self.client.post(path=f"{BASE_PATH}/api/sensor/", format="json", data=payload)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual("Test Sensor 1", response.data.get('name'))
        self.assertEqual("Celsius", response.data.get('unit'))

    def test_get_sensor(self) -> None:

        sensor_name: str = "Test Sensor 2"
        sensor_unit: str = "Fahrenheit"

        created_sensor: Sensor = Sensor.objects.create(name=sensor_name, unit=sensor_unit)
        created_sensor_id = created_sensor.id

        response: Response = self.client.get(f"{BASE_PATH}/api/sensor/{created_sensor_id}/")

        expected_name: str = response.data.get('name')
        expected_unit: str = response.data.get('unit')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_name, sensor_name)
        self.assertEqual(expected_unit, sensor_unit)
