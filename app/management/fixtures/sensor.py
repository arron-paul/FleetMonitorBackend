from dataclasses import dataclass

from app.models import UNIT_CHOICES_CELSIUS, UNIT_CHOICES_FAHRENHEIT


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
    SensorFixture("Front Temperature", UNIT_CHOICES_CELSIUS),
    SensorFixture("Transformer Temperature", UNIT_CHOICES_FAHRENHEIT),
    SensorFixture("Generator Temperature", UNIT_CHOICES_CELSIUS),
    SensorFixture("Gearbox Temperature", UNIT_CHOICES_FAHRENHEIT),
    SensorFixture("Blade Temperature", UNIT_CHOICES_FAHRENHEIT),
    SensorFixture("Brake Temperature", UNIT_CHOICES_CELSIUS),
    SensorFixture("Main Bearing Temperature", UNIT_CHOICES_CELSIUS),
    SensorFixture("Hydraulic Temperature", UNIT_CHOICES_CELSIUS)
]
