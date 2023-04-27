from django_filters import rest_framework as filters

from app.models import SensorRecord


class SensorRecordFilter(filters.FilterSet):
    """
    Provides filtering of sensor record fields using query parameters
    """
    sensor = filters.CharFilter(field_name='sensor__name')
    date_from = filters.DateTimeFilter(field_name='date', lookup_expr='gte')
    date_to = filters.DateTimeFilter(field_name='date', lookup_expr='lte')
    value_min = filters.NumberFilter(field_name='value', lookup_expr='gte')
    value_max = filters.NumberFilter(field_name='value', lookup_expr='lte')

    class Meta:
        model = SensorRecord
        fields = [
            'sensor',
            'date_from',
            'date_to',
            'value_min',
            'value_max'
        ]
