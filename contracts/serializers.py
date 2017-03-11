from rest_framework import serializers

from applications.serializers import ApplicationSerializer
from .models import Contract
from shared.models import Client


class ContractSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(source='application.client', queryset=Client.objects.all())
    application_data = ApplicationSerializer(source='application', read_only=True)

    class Meta:
        model = Contract
        fields = ('id', 'application', 'application_data', 'number', 'date', 'finish_date', 'price', 'terms', 'poa',
                  'poa_number', 'poa_date', 'client')
