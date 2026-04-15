from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.models import Category, Medicine, Supplier, Country, City
from apps.serializers import (CategoryModelSerializer, MedicineModelSerializer,
                             MedicineUpdateModelSerializer, SupplierModelSerializer, CountryModelSerializer,
                             CityModelSerializer)


@extend_schema(tags=['Category'])
class CategoryListCreateApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

@extend_schema(tags=['Medicine'])
class MedicineListCreateApiView(ListCreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineModelSerializer

@extend_schema(tags=['Medicine'])
class MedicineRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineUpdateModelSerializer
    lookup_field = 'id'
    search_fields = ['name']

@extend_schema(tags=['Supplier'])
class SupplierListCreateAPIView(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierModelSerializer

@extend_schema(tags=['Country'])
class CountryListAPIView(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer

@extend_schema(tags=['City'])
class CityListCreateApiView(ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CityModelSerializer





