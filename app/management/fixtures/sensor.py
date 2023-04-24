from dataclasses import dataclass

from app.units import UNIT_CHOICE_CELSIUS, UNIT_CHOICE_FAHRENHEIT


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
    SensorFixture("Sensor 1", UNIT_CHOICE_CELSIUS),
    SensorFixture("Sensor 2", UNIT_CHOICE_CELSIUS),
    SensorFixture("Sensor 3", UNIT_CHOICE_FAHRENHEIT)
]