from rest_framework import serializers

from app.models import UNIT_CHOICES


class TemperatureUnitChoiceField(serializers.Field):
    """
    Custom DRF Field to convert between internal value of `unit` and it's
    string representation as defined in UNIT_CHOICES
    https://www.django-rest-framework.org/api-guide/fields/#custom-fields
    """

    def to_representation(self, unit_internal_value: int):
        """
        Converts the internal value of the `unit` field to its string representation.
        """
        return dict(UNIT_CHOICES)[unit_internal_value]

    def to_internal_value(self, choice: str):
        """
        Converts the string representation of the `unit` field, such as 'Celsius'
        back to its stored integer value.
        """
        for unit_choice in UNIT_CHOICES:
            if unit_choice[1] == choice:
                return unit_choice[0]
        raise serializers.ValidationError('Invalid unit choice')
