from rest_framework import serializers

from app.models import TEMPERATURE_CHOICES


class TemperatureUnitChoiceField(serializers.Field):
    """
    Custom field to convert between internal value of the sensor unit,
    and it's string representation.
    """

    def to_representation(self, internal_value: int):
        """
        Converts internal value of `unit` field to its string representation.
        """
        return dict(TEMPERATURE_CHOICES)[internal_value]

    def to_internal_value(self, string_representation: str):
        """
        Converts string representation of `unit` field to its internal integer value.
        """
        for unit_choice in TEMPERATURE_CHOICES:
            if unit_choice[1] == string_representation:
                return unit_choice[0]
        raise serializers.ValidationError('temperature unit not supported')
