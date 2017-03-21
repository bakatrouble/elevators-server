from rest_framework import serializers

from .models import Contract


class ContractSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(source='application.client', read_only=True)

    class Meta:
        model = Contract
        fields = ('id', 'application', 'number', 'date', 'price', 'advance', 'terms', 'poa_client',
                  'poa_client_number', 'poa_client_date', 'poa_contractor', 'poa_contractor_number',
                  'poa_contractor_date', 'client')
