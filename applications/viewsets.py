from django_filters import FilterSet, CharFilter, DateFilter
from django_filters.rest_framework import DjangoFilterBackend
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
    filter_backends = (DjangoFilterBackend,)

    # noinspection PyPep8Naming
    class filter_class(FilterSet):
        contract_number = CharFilter(name='contract__number', lookup_expr='icontains')
        contract_date = DateFilter(name='contract__date')

        class Meta:
            model = Application
            fields = 'contract_number', 'contract_date',

    # noinspection PyPep8Naming
    class pagination_class(pagination.CursorPagination):
        ordering = '-id'


class ApplicationEntryViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationEntrySerializer
    queryset = ApplicationEntry.objects.all()
