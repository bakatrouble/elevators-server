from rest_framework import serializers

from .models import Application, ApplicationEntry, ApplicationType


class ApplicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationType
        fields = ('id', 'name', 'hints', 'application_template', 'contract_template', 'order_template',)


class ApplicationEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationEntry
        fields = ('id', 'address_oblast', 'address_raion', 'address_city', 'address_street',
                  'address_house', 'address_building', 'address_letter', 'purpose', 'number', 'maker', 'load', 'stops',
                  'speed', 'date', 'replacements', 'deadline',)


class ApplicationSerializer(serializers.ModelSerializer):
    entries = ApplicationEntrySerializer(many=True)

    class Meta:
        model = Application
        fields = ('id', 'date', 'type', 'client', 'entries')

    def create(self, validated_data):
        entries = validated_data.pop('entries')
        application = Application.objects.create(**validated_data)
        for entry in entries:
            ApplicationEntry.objects.create(application=application, **entry)
        return application

    def update(self, instance: Application, validated_data):
        ApplicationEntry.objects.filter(application=instance).delete()
        entries = validated_data.pop('entries')
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        for entry in entries:
            ApplicationEntry.objects.create(application=instance, **entry)
        instance.save()
        return instance
