from rest_framework import serializers

from .models import Client, Specialist


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'full_name', 'short_name', 'registration_address', 'location_address', 'phone', 'inn', 'kpp',
                  'account_number', 'bank', 'bik', 'ogrn', 'person_name', 'person_post',)


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ('id', 'last_name', 'first_name', 'patr_name',)
