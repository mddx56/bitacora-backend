from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import UserAccountView, GroupListCreateAPIView

# router = routers.DefaultRouter()

urlpatterns = [
    # path("", include(router.urls)),
    path("users/", UserAccountView.as_view(), name="user_list"),
    path("groups/", GroupListCreateAPIView.as_view(), name="group_list"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verify/", TokenVerifyView.as_view(), name="token_verify"),
]

# ojo
