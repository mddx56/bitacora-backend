from django.urls import include, path
from rest_framework import routers
from apps.transaction.views import CategorySerializer, TransactionView

router = routers.DefaultRouter()
# router.register("category", CategorySerializer)
router.register("", TransactionView)

urlpatterns = [
    path("", include(router.urls)),
]
