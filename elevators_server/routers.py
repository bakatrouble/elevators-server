from rest_framework import routers

from contracts.viewsets import ContractViewSet
from shared.viewsets import ClientViewSet
from applications.viewsets import ApplicationViewSet, ApplicationEntryViewSet, ApplicationTypeViewSet

router = routers.DefaultRouter()
router.register('clients', ClientViewSet)
router.register('applications', ApplicationViewSet)
router.register('application_entries', ApplicationEntryViewSet)
router.register('application_types', ApplicationTypeViewSet)
router.register('contracts', ContractViewSet)

urlpatterns = router.urls
