from rest_framework import routers

from accounts.viewsets import AccountViewSet
from contracts.viewsets import ContractViewSet
from orders.viewsets import OrderViewSet
from shared.viewsets import ClientViewSet, SpecialistViewSet
from applications.viewsets import ApplicationViewSet, ApplicationTypeViewSet

router = routers.DefaultRouter()
router.register('applications', ApplicationViewSet)
router.register('contracts', ContractViewSet)
router.register('accounts', AccountViewSet)
router.register('orders', OrderViewSet)

router.register('clients', ClientViewSet)
router.register('application_types', ApplicationTypeViewSet)
router.register('specialists', SpecialistViewSet)

urlpatterns = router.urls
