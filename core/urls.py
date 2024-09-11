from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("apps.authrole.urls")),
    path("api/card/", include("apps.card.urls")),
    path("api/bank/", include("apps.bank.urls")),
]
