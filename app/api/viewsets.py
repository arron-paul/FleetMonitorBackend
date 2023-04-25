from rest_framework import viewsets

from app.api.filters import SensorRecordFilter
from app.api.serializers import SensorSerializer, SensorRecordSerializer
from app.models import Sensor, SensorRecord


class SensorViewSet(viewsets.ModelViewSet):
    """
    Viewset for Sensor model
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorRecordViewSet(viewsets.ModelViewSet):
    """
    Viewset for Sensor model
    """
    queryset = SensorRecord.objects.all()
    serializer_class = SensorRecordSerializer
    filterset_class = SensorRecordFilter
