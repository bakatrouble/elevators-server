from rest_framework import serializers

from contracts.models import Contract


class ContractSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(source='application.client')

    class Meta:
        model = Contract
        fields = ('id', 'application', 'number', 'date', 'finish_date', 'price', 'terms', 'poa', 'poa_number',
                  'poa_date', 'client')
