from rest_framework import serializers

from .models import Application, ApplicationEntry, ApplicationType


class ApplicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationType
        fields = ('id', 'name', 'hints', 'application_template', 'contract_template', 'order_template',)


class ApplicationEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationEntry
        fields = ('id', 'application', 'address_oblast', 'address_raion', 'address_city', 'address_street',
                  'address_house', 'address_building', 'address_letter', 'purpose', 'number', 'maker', 'load', 'stops',
                  'speed', 'date', 'replacements', 'deadline',)


class ApplicationSerializer(serializers.ModelSerializer):
    entries = ApplicationEntrySerializer(many=True, read_only=True)

    class Meta:
        model = Application
        fields = ('date', 'type', 'client', 'entries')
