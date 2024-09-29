from django.urls import path
from apps.bank import views

urlpatterns = [
    path("list/", views.BankListView, name="Bank list"),
    # path("list/", views.BankListAPIView.as_view(), name="Bank list"),
    path("create/", views.BankCreateAPIView.as_view(), name="Bank create"),
    path("update/<pk>/", views.BankUpdateAPIView.as_view(), name="Config update"),
    path("get/<int:id>", views.BankRetrieveView, name="Bank get"),
]
