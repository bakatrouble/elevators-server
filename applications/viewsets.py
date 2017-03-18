from rest_framework import viewsets, pagination

from .serializers import ApplicationTypeSerializer, ApplicationSerializer, ApplicationEntrySerializer
from .models import ApplicationType, ApplicationEntry, Application


class ApplicationTypeViewSet(viewsets.ModelViewSet):
    pagination_class = None
    serializer_class = ApplicationTypeSerializer
    queryset = ApplicationType.objects.all()


class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()

    class pagination_class(pagination.CursorPagination):
        ordering = '-id'


class ApplicationEntryViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationEntrySerializer
    queryset = ApplicationEntry.objects.all()
