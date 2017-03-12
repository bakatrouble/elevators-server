from rest_framework import viewsets

from .serializers import ClientSerializer, SpecialistSerializer
from .models import Client, Specialist


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class SpecialistViewSet(viewsets.ModelViewSet):
    serializer_class = SpecialistSerializer
    queryset = Specialist.objects.all()
