from rest_framework import serializers

from .models import Contract
from shared.models import Client


class ContractSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(source='application.client', queryset=Client.objects.all())

    class Meta:
        model = Contract
        fields = ('id', 'application', 'number', 'date', 'finish_date', 'price', 'terms', 'poa', 'poa_number',
                  'poa_date', 'client')
