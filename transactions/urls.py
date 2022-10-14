from django.urls import path

from . import views

urlpatterns = [
    path("upload/", views.upload_file, name="upload-file"),
    path("transactions/<store_name>/", views.list_transactions_by_store, name="list-transactions"),
    path("search-results/", views.filter_stores, name="filter-stores"),

]