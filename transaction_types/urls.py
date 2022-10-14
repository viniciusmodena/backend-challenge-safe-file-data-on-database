from django.urls import path

from . import views

urlpatterns = [
    path("transaction-types/", views.TransactionTypesView.as_view(), name="list-transaction-types"),
]