from rest_framework import serializers

from accounts.serializers import AccountSerializer
from contracts.serializers import ContractSerializer
from orders.serializers import OrderSerializer
from shared.models import Client
from .models import Application, ApplicationEntry, ApplicationType


class ApplicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationType
        fields = ('id', 'name', 'hints', 'application_template', 'contract_template', 'account_template',
                  'order_template',)


class ApplicationEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationEntry
        fields = ('id', 'address_oblast', 'address_raion', 'address_city', 'address_street',
                  'address_house', 'address_building', 'address_letter', 'purpose', 'number', 'maker', 'load', 'stops',
                  'speed', 'date', 'replacements', 'deadline',)


class ApplicationSerializer(serializers.ModelSerializer):
    entries = ApplicationEntrySerializer(many=True)
    contract = ContractSerializer(source='get_contract', read_only=True)
    account = AccountSerializer(source='get_account', read_only=True)
    order = OrderSerializer(source='get_order', read_only=True)
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), allow_null=True)

    class Meta:
        model = Application
        fields = 'id', 'date', 'type', 'client', 'entries', 'contract', 'account', 'order'  # , 'protocols',

    def create(self, validated_data):
        entries = validated_data.pop('entries')
        if validated_data['client'] is None:
            validated_data['client'] = Client.objects.create(short_name='<без названия>')
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
