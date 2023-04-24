from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from app.api.filters import SensorRecordFilter
from app.api.serializers import SensorSerializer, SensorRecordSerializer
from app.models import Sensor, SensorRecord


class SensorViewSet(viewsets.ModelViewSet):
    """
    Viewset for Sensor model
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def list(self, request, **kwargs):
        serializer = SensorSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        sensor = get_object_or_404(self.queryset, pk=pk)
        serializer = SensorSerializer(sensor)
        return Response(serializer.data)


class SensorRecordViewSet(viewsets.ModelViewSet):
    """
    Viewset for Sensor model
    """
    queryset = SensorRecord.objects.all()
    serializer_class = SensorRecordSerializer
    filterset_class = SensorRecordFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data))
