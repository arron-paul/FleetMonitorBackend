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
    SensorFixture("Front Temperature Sensor", UNIT_CHOICES_CELSIUS),
    SensorFixture("Transformer Temperature Sensor", UNIT_CHOICES_FAHRENHEIT),
    SensorFixture("Generator Temperature Sensor", UNIT_CHOICES_CELSIUS),
    SensorFixture("Gearbox Temperature Sensor", UNIT_CHOICES_FAHRENHEIT),
    SensorFixture("Blade Temperature Sensor", UNIT_CHOICES_FAHRENHEIT),
    SensorFixture("Brake Temperature Sensor", UNIT_CHOICES_CELSIUS),
    SensorFixture("Bearing Temperature Sensor", UNIT_CHOICES_CELSIUS),
    SensorFixture("Hydraulic Temperature Sensor", UNIT_CHOICES_CELSIUS)
]
