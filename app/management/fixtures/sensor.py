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
    SensorFixture("Front Temperature Sensor", "Celsius"),
    SensorFixture("Transformer Temperature Sensor", "Fahrenheit"),
    SensorFixture("Generator Temperature Sensor", "Celsius"),
    SensorFixture("Gearbox Temperature Sensor", "Fahrenheit"),
    SensorFixture("Blade Temperature Sensor", "Fahrenheit"),
    SensorFixture("Brake Temperature Sensor", "Celsius"),
    SensorFixture("Bearing Temperature Sensor", "Celsius"),
    SensorFixture("Hydraulic Temperature Sensor", "Celsius"),
]
