from django_filters import rest_framework as filters, Filter

from app.models import SensorRecord


class SensorRecordFilter(filters.FilterSet):
    """
    FilterSet that provides filtering of properties for SensorRecord using query parameters.
    https://www.django-rest-framework.org/api-guide/filtering/#setting-filter-backends
    https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html#integration-with-drf
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
