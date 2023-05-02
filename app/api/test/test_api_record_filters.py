from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase


class TestSensorRecordFilters(APITestCase):

    def setUp(self) -> None:
        # Create several sensors before records are added to them
        sensors: list = [
            ('Generic Sensor 1', 'Celsius'),
            ('Generic Sensor 2', 'Fahrenheit'),
            ('Main Bearing Temperature 1', 'Celsius'),
            ('Main Bearing Temperature 2', 'Celsius')
        ]
        for sensor in sensors:
            response: Response = self.client.post(
                path=f'/api/sensor/',
                format='json',
                data={'name': sensor[0], 'unit': sensor[1]})
            self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_filtering_sensor_name(self):
        """
        Ensure filtering of `sensor` query parameter is valid
        """
        record_gs1: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': 'Generic Sensor 1',
                'date': '2023-04-25T17:01:05.139017Z',
                'value': 12.0
            })
        record_gs2: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': 'Generic Sensor 2',
                'date': '2023-04-25T17:01:05.139017Z',
                'value': 12.0
            })
        record_mbt1: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': 'Main Bearing Temperature 1',
                'date': '2023-04-25T17:01:05.139017Z',
                'value': 12.0
            })
        record_mbt2: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': 'Main Bearing Temperature 2',
                'date': '2023-04-25T17:01:05.139017Z',
                'value': 12.0
            })

        self.assertEqual(status.HTTP_201_CREATED, record_gs1.status_code)
        self.assertEqual(status.HTTP_201_CREATED, record_gs2.status_code)
        self.assertEqual(status.HTTP_201_CREATED, record_mbt1.status_code)
        self.assertEqual(status.HTTP_201_CREATED, record_mbt2.status_code)

        # Ensure when querying for sensor 'Generic Sensor 1' that only returns that one sensor
        name_filter: Response = self.client.get( f'/api/data/?sensor=Generic Sensor 1')
        self.assertEqual(status.HTTP_200_OK, name_filter.status_code)
        self.assertIsInstance(name_filter.json(), list)
        self.assertEqual(len(name_filter.json()), 1)
        self.assertEqual(name_filter.json()[0].get('sensor'), 'Generic Sensor 1')

    def test_filtering_sensor_dates(self):
        """
        Ensure filtering of `date_from` and `date_to` query parameters is valid
        """
        record_gs1: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': 'Generic Sensor 1',
                'date': '2023-01-01T01:01:01.000000Z',
                'value': 12.0
            })
        record_gs2: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': 'Generic Sensor 1',
                'date': '2023-01-02T01:01:01.000000Z',
                'value': 12.0
            })
        record_gs3: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': 'Generic Sensor 1',
                'date': '2023-01-03T01:01:01.000000Z',
                'value': 12.0
            })
        record_gs4: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': 'Generic Sensor 1',
                'date': '2023-01-04T01:01:01.000000Z',
                'value': 12.0
            })

        self.assertEqual(status.HTTP_201_CREATED, record_gs1.status_code)
        self.assertEqual(status.HTTP_201_CREATED, record_gs2.status_code)
        self.assertEqual(status.HTTP_201_CREATED, record_gs3.status_code)
        self.assertEqual(status.HTTP_201_CREATED, record_gs4.status_code)

        # Ensure when querying for date_from, date_to, covering a date range that
        # includes all records above, that we retrieve all 4 records
        date_filter_one: Response = self.client.get(
            f'/api/data/?date_from=2023-01-01T01:01:01.000000Z&date_to=2023-01-04T01:01:01.000000Z')
        self.assertEqual(status.HTTP_200_OK, date_filter_one.status_code)
        self.assertIsInstance(date_filter_one.json(), list)
        self.assertEqual(len(date_filter_one.json()), 4)

        # Ensure when querying for date_from, date_to, covering a date range that
        # includes the most recent 2 records, that we get those 2 records only
        date_filter_two: Response = self.client.get(
            f'/api/data/?date_from=2023-01-03T01:01:01.000000Z&date_to=2023-01-04T01:01:01.000000Z')
        self.assertEqual(status.HTTP_200_OK, date_filter_two.status_code)
        self.assertIsInstance(date_filter_two.json(), list)
        self.assertEqual(len(date_filter_two.json()), 2)

    def test_filtering_sensor_values(self):
        """
        Ensure filtering of `value_min` and `value_max` query parameters are valid
        """
        record_gs1: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': 'Generic Sensor 1',
                'date': '2023-01-01T01:01:01.000000Z',
                'value': 12.0
            })
        record_gs2: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': 'Generic Sensor 1',
                'date': '2023-01-01T01:01:01.000000Z',
                'value': 20.0
            })
        record_gs3: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': 'Generic Sensor 1',
                'date': '2023-01-01T01:01:01.000000Z',
                'value': 20.0
            })
        record_gs4: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': 'Generic Sensor 1',
                'date': '2023-01-01T01:01:01.000000Z',
                'value': 40.0
            })

        self.assertEqual(status.HTTP_201_CREATED, record_gs1.status_code)
        self.assertEqual(status.HTTP_201_CREATED, record_gs2.status_code)
        self.assertEqual(status.HTTP_201_CREATED, record_gs3.status_code)
        self.assertEqual(status.HTTP_201_CREATED, record_gs4.status_code)

        # Ensure when querying for value_min, value_max, covering a value range that
        # includes all records above, that we retrieve all 4 records
        filter_min_10_max_50: Response = self.client.get(
            f'/api/data/?value_min=10.0&value_max=50.0')
        self.assertEqual(status.HTTP_200_OK, filter_min_10_max_50.status_code)
        self.assertIsInstance(filter_min_10_max_50.json(), list)
        self.assertEqual(len(filter_min_10_max_50.json()), 4)

        # Ensure when querying for value_min, value_max, covering a value range
        # between 18.0 and 24.0, we get 2 results back.
        filter_min_18_max_24: Response = self.client.get(
            f'/api/data/?value_min=20.0&value_max=20.0')
        self.assertEqual(status.HTTP_200_OK, filter_min_18_max_24.status_code)
        self.assertIsInstance(filter_min_18_max_24.json(), list)
        self.assertEqual(len(filter_min_18_max_24.json()), 2)

        # Ensure when querying for value_min of 35.0, we get one result
        filter_min_35: Response = self.client.get(
            f'/api/data/?value_min=35.0')
        self.assertEqual(status.HTTP_200_OK, filter_min_35.status_code)
        self.assertIsInstance(filter_min_35.json(), list)
        self.assertEqual(len(filter_min_35.json()), 1)

        # Ensure when querying for value_max of 35.0, we get three results
        filter_min_35: Response = self.client.get(
            f'/api/data/?value_max=35.0')
        self.assertEqual(status.HTTP_200_OK, filter_min_35.status_code)
        self.assertIsInstance(filter_min_35.json(), list)
        self.assertEqual(len(filter_min_35.json()), 3)

    def test_filtering_multiple_query(self):
        """
        Ensure filtering of all query parameters at once is valid
        """
        record_gs1: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': 'Generic Sensor 1',
                'date': '2023-01-01T01:01:01.000000Z',
                'value': 12.0
            })
        record_gs2: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': 'Generic Sensor 2',
                'date': '2023-01-01T01:01:01.000000Z',
                'value': 20.0
            })
        record_gs3: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': 'Generic Sensor 2',
                'date': '2023-01-01T01:01:01.000000Z',
                'value': 20.0
            })
        record_gs4: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': 'Generic Sensor 2',
                'date': '2024-01-01T01:01:01.000000Z',
                'value': 43.5
            })
        record_gs5: Response = self.client.post(
            path=f'/api/data/',
            format='json',
            data={
                'sensor': 'Generic Sensor 2',
                'date': '2024-01-02T01:01:01.000000Z',
                'value': 43.0
            })

        self.assertEqual(status.HTTP_201_CREATED, record_gs1.status_code)
        self.assertEqual(status.HTTP_201_CREATED, record_gs2.status_code)
        self.assertEqual(status.HTTP_201_CREATED, record_gs3.status_code)
        self.assertEqual(status.HTTP_201_CREATED, record_gs4.status_code)
        self.assertEqual(status.HTTP_201_CREATED, record_gs5.status_code)

        # Ensure when querying with a `sensor` of 'Generic Sensor 2' with a `value_min`
        # of 42.0 and a `value_max` of 44.0 and a `date_to` of 2024-01-01T01:01:01.000000Z
        # and a `date_from` of 2024-01-02T01:01:01.000000Z - we should receive 2 results
        all_possible_filters: Response = self.client.get(
            f'/api/data/'
            f'?sensor=Generic%20Sensor%202'
            f'&value_min=42.0'
            f'&value_max=44.0'
            f'&date_from=2024-01-01T01:01:01.000000Z'
            f'&date_to=2024-01-02T01:01:01.000000Z')
        self.assertEqual(status.HTTP_200_OK, all_possible_filters.status_code)
        self.assertIsInstance(all_possible_filters.json(), list)
        self.assertEqual(len(all_possible_filters.json()), 2)
