from dataclasses import dataclass

from app.models import TEMPERATURE_CHOICE_CELSIUS, TEMPERATURE_CHOICE_FAHRENHEIT


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
    SensorFixture("Front Temperature", TEMPERATURE_CHOICE_CELSIUS),
    SensorFixture("Transformer Temperature", TEMPERATURE_CHOICE_FAHRENHEIT),
    SensorFixture("Generator Temperature", TEMPERATURE_CHOICE_CELSIUS),
    SensorFixture("Gearbox Temperature", TEMPERATURE_CHOICE_FAHRENHEIT),
    SensorFixture("Blade Temperature", TEMPERATURE_CHOICE_FAHRENHEIT),
    SensorFixture("Brake Temperature", TEMPERATURE_CHOICE_CELSIUS),
    SensorFixture("Main Bearing Temperature", TEMPERATURE_CHOICE_CELSIUS),
    SensorFixture("Hydraulic Temperature", TEMPERATURE_CHOICE_CELSIUS)
]
