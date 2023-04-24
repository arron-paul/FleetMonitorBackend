from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase

API_BASE_PATH = "/api"


class TestSensorViewSet(APITestCase):

    def test_create_sensor(self):

        response: Response = self.client.post(
            path=f"{API_BASE_PATH}/sensor",
            data={
                "name": "Test Sensor 1",
                "unit": "Celsius"
            },
            format="json"
        )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        self.assertEqual("Test Sensor 1", response.data.get('name'))
        self.assertEqual("Celsius", response.data.get('unit'))

