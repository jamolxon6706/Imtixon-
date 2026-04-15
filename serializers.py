from rest_framework.serializers import ModelSerializer

from apps.models import Category, Medicine, Supplier, City, Country


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')

class MedicineModelSerializer(ModelSerializer):
    class Meta:
        model = Medicine
        fields = ('id','name','category','description','price','stock')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')

        if request and request.method == 'GET': # noqa
            representation.pop('description', None)

        return representation

class MedicineUpdateModelSerializer(ModelSerializer):
    class Meta:
        model = Medicine
        fields = ('id','name','category','description','price','stock')


class SupplierModelSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id','name','phone','city',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')

        if request and request.method == 'GET': # noqa
            representation['city'] = instance.city.name


        return representation


class CountryModelSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ('id','name')

class CityModelSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ('id','name','country')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')

        if request and request.method == 'GET': # noqa
            representation['country'] = instance.country.name

        return representation
