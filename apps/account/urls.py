from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import (
    UserAccountView,
    GroupListCreateAPIView,
    ObtainTokenPairView,
    UserRetrieveView,
    ChangePasswordView,
)


urlpatterns = [
    path("users/", UserAccountView.as_view(), name="user_list"),
    path("user/<int:id>/", UserRetrieveView.as_view(), name="user_get"),
    path("groups/", GroupListCreateAPIView.as_view(), name="group_list"),
    path("login/", ObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
]

# ojo
