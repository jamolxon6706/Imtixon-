from django.contrib import admin
from django.urls import path

from apps.views import (CategoryListCreateApiView, MedicineListCreateApiView,
                       MedicineRetrieveUpdateDestroyApiView, SupplierListCreateAPIView,
                       CountryListAPIView, CityListCreateApiView)

urlpatterns = [
    path('category',CategoryListCreateApiView.as_view()),
    path('medicine',MedicineListCreateApiView.as_view()),
    path('medicine/<int:id>',MedicineRetrieveUpdateDestroyApiView.as_view()),
    path('supplier',SupplierListCreateAPIView.as_view()),
    path('country',CountryListAPIView.as_view()),
    path('city',CityListCreateApiView.as_view()),
]