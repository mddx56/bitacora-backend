from django.urls import include, path
from rest_framework import routers
from apps.card.views import CardView

router = routers.DefaultRouter()
router.register("", CardView)
urlpatterns = [
    path("", include(router.urls)),
]
