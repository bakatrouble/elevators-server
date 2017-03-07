from rest_framework import viewsets

from .serializers import ApplicationTypeSerializer, ApplicationSerializer, ApplicationEntrySerializer
from .models import ApplicationType, ApplicationEntry, Application


class ApplicationTypeViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationTypeSerializer
    queryset = ApplicationType.objects.all()


class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()


class ApplicationEntryViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationEntrySerializer
    queryset = ApplicationEntry.objects.all()
