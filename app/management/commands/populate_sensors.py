from django.core.management.base import BaseCommand

from app.management.fixtures.sensor import SensorFixture
from app.models import Sensor


class Command(BaseCommand):
    help = 'Creates Sensors'

    def handle(self, *args, **options):
        for sensor_fixture in SensorFixture.get_fixtures():
            Sensor.objects.create(name=sensor_fixture.name, unit=sensor_fixture.unit)
            self.stdout.write(f"Created Sensor `{sensor_fixture.name}`")
