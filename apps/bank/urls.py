from django.urls import include, path
from rest_framework import routers
from apps.bank import views

urlpatterns = [
    path("list/", views.BankListAPIView.as_view(), name="Bank list"),
    path("create/", views.BankCreateAPIView.as_view(), name="Bank create"),
    path("update/<pk>", views.BankUpdateAPIView.as_view(), name="Bank update"),
    path("get/<pk>", views.BankRetrieveAPIView.as_view(), name="Bank get"),
]
