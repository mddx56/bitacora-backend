from django.urls import include, path
from rest_framework import routers
from apps.transaction import views


urlpatterns = [
    path("", views.TransactionView.as_view(), name="Transaccion"),
    path("category/", views.CategoryView.as_view(), name="Categoria"),
    path("devit/", views.DebitCard, name="Devitar tarjeta"),
    path("credit/", views.CreditCard, name="Credito tarjeta"),
]
