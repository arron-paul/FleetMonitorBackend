from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Flushes existing data and re-creates Sensors and SensorRecords'

    def handle(self, *args, **options):

        # Delete all rows in the database
        call_command('flush', interactive=False)

        # Populate Sensors
        call_command('populate_sensors')
        call_command('populate_sensor_records')
