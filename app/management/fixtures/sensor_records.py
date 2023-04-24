from dataclasses import dataclass


@dataclass
class SensorRecordFixture:
    """
    Bare-bones fixture data that represents a SensorRecord
    """
    timestamp: str
    sensor_name: str
    value: float

    @staticmethod
    def get_fixtures():
        sensors_records = []
        for sensor_record_fixture in SENSOR_RECORDS_FIXTURES:
            sensors_records.append(sensor_record_fixture)
        return sensors_records


SENSOR_RECORDS_FIXTURES = [
    SensorRecordFixture("2022-04-27T12:13:00Z", "Sensor 1", 12.0),
    SensorRecordFixture("2022-04-27T12:14:00Z", "Sensor 1", 14.0),
    SensorRecordFixture("2022-04-27T12:15:00Z", "Sensor 1", 18.0),
    SensorRecordFixture("2022-04-27T12:14:00Z", "Sensor 2", 31.0),
    SensorRecordFixture("2022-04-27T12:19:00Z", "Sensor 2", 27.0),
    SensorRecordFixture("2022-04-27T12:25:00Z", "Sensor 2", 27.0),
    SensorRecordFixture("2022-04-27T12:07:00Z", "Sensor 3", 17.0),
    SensorRecordFixture("2022-04-27T12:11:00Z", "Sensor 3", 19.0),
    SensorRecordFixture("2022-04-27T12:15:00Z", "Sensor 3", 13.0),
]