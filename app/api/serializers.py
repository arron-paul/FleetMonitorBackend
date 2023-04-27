from rest_framework import serializers

from app.api.fields import TemperatureUnitChoiceField
from app.models import Sensor, SensorRecord


class SensorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Sensor model
    """

    # Unit internal value is an integer, override unit field
    # such that it returns the unit choice string representation
    unit = TemperatureUnitChoiceField()

    class Meta:
        model = Sensor
        fields = ['name', 'unit']


class SensorRecordSerializer(serializers.ModelSerializer):
    """
    Serializer for the SensorRecord model
    """

    sensor = serializers.CharField(source='sensor.name')

    class Meta:
        model = SensorRecord
        fields = ['sensor', 'date', 'value']

    def create(self, validated_data):
        # We are providing the sensor name instead of PK
        sensor_name: str = validated_data.pop('sensor').get('name')
        if sensor_name is None:
            raise AssertionError('Sensor name is required')
        sensor: Sensor = Sensor.objects.get(name=sensor_name)
        return SensorRecord.objects.create(sensor=sensor, **validated_data)
