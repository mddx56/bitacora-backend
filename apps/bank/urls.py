from django.urls import include, path
from rest_framework import routers
from apps.bank.views import BankView

router = routers.DefaultRouter()
router.register("", BankView)
urlpatterns = [
    path("", include(router.urls)),
]
