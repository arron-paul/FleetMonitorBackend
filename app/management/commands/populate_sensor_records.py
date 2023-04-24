from django.core.management.base import BaseCommand

from app.management.fixtures.sensor_records import SensorRecordFixture
from app.models import SensorRecord, Sensor


class Command(BaseCommand):
    help = 'Creates several SensorRecords for each Sensor'

    def handle(self, *args, **options):
        for sensor_record_fixture in SensorRecordFixture.get_fixtures():
            SensorRecord.objects.create(
                sensor=Sensor.objects.get(name=sensor_record_fixture.sensor_name),
                date=sensor_record_fixture.date,
                value=sensor_record_fixture.value
            )
            self.stdout.write(f"Created Sensor Record for `{sensor_record_fixture.sensor_name}`")
