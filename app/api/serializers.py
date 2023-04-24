from rest_framework import serializers

from app.models import Sensor, SensorRecord


class SensorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Sensor model
    """
    class Meta:
        model = Sensor
        fields = ['name', 'unit']


class SensorRecordSerializer(serializers.ModelSerializer):
    """
    Serializer for the SensorRecord model
    """
    sensor_name = serializers.ReadOnlyField(source='sensor.name')

    class Meta:
        model = SensorRecord
        fields = ['date', 'sensor_name', 'value']
