from django.urls import include, path
from rest_framework import routers
from apps.transaction import views


urlpatterns = [
    path("", views.TransactionView.as_view(), name="Transaccion"),
    path("category/", views.CategoryView.as_view(), name="Categoria"),
    path("credit/", views.DebitCard, name="Credito tarjeta"),
    path("devit/", views.CreditCard, name="Devitar tarjeta"),
]
