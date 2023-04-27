import datetime
import random

import pytz
from django.core.management import call_command
from django.core.management.base import BaseCommand

from app.management.fixtures.sensor import SensorFixture
from app.models import SensorRecord, Sensor

DATE_FROM = datetime.datetime(2021, 1, 1, tzinfo=pytz.timezone('UTC'))
DATE_TO = datetime.datetime(2023, 12, 31, tzinfo=pytz.timezone('UTC'))
VALUE_MIN = 25.0
VALUE_MAX = 100.0


class Command(BaseCommand):
    help = 'Flushes existing data and re-creates sensors and optional sensor records'

    def add_arguments(self, parser):
        parser.add_argument('--records', type=int, help='The amount of sensor records for each sensor')

    def handle(self, *args, **options):

        # Delete all rows in the database
        call_command('flush', interactive=False)

        # Create sensors
        for sensor_fixture in SensorFixture.get_fixtures():
            Sensor.objects.create(name=sensor_fixture.name, unit=sensor_fixture.unit)
            self.stdout.write(f"Created sensor `{sensor_fixture.name}`")

        # Optionally populate sensor records
        if options.get('records'):
            num_records: int = options.get('records')

            # Iterate through created sensors
            for sensor in Sensor.objects.all():
                self.stdout.write(f"Creating {num_records} sensor records for Sensor `{sensor.name}`")

                for i in range(num_records):

                    # Random date and value
                    random_seconds: int = random.randint(0, int((DATE_TO - DATE_FROM).total_seconds()))
                    random_datetime: datetime = DATE_FROM + datetime.timedelta(seconds=random_seconds)
                    random_value: float = random.uniform(VALUE_MIN, VALUE_MAX)

                    # Create a random sensor record
                    SensorRecord.objects.create(
                        sensor=sensor,
                        date=random_datetime,
                        value=random_value)
