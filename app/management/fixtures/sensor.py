from dataclasses import dataclass

@dataclass
class SensorFixture:
    """
    Bare-bones fixture data that represents a Sensor
    """
    name: str
    unit: str

    @staticmethod
    def get_fixtures():
        sensors = []
        for sensor_fixture in SENSOR_FIXTURES:
            sensors.append(sensor_fixture)
        return sensors


SENSOR_FIXTURES = [
    SensorFixture("Sensor 1", "Celsius"),
    SensorFixture("Sensor 2", "Celsius"),
    SensorFixture("Sensor 3", "Fahrenheit")
]