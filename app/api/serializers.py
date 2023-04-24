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
    class Meta:
        model = SensorRecord
        fields = ['timestamp', 'sensor', 'value']
