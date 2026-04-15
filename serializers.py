from rest_framework import serializers
from .models import Category, Medicine, Country, City, Supplier, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class MedicineSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category'
    )

    class Meta:
        model = Medicine
        fields = ['id', 'name', 'category_id', 'description', 'price', 'stock', 'expiry_date']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class CitySerializer(serializers.ModelSerializer):
    country_id = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(), source='country'
    )

    class Meta:
        model = City
        fields = ['id', 'name', 'country_id']


class SupplierSerializer(serializers.ModelSerializer):
    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(), source='city'
    )

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'phone', 'city_id']


# Buyurtma ichidagi dorilar uchun yordamchi serializer
class OrderItemSerializer(serializers.ModelSerializer):
    medicine_id = serializers.PrimaryKeyRelatedField(
        queryset=Medicine.objects.all(), source='medicine'
    )

    class Meta:
        model = OrderItem
        fields = ['medicine_id', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'total_price', 'status', 'created_at', 'items']
        read_only_fields = ['total_price', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')

        # Dastlab buyurtmani umumiy narxsiz yaratamiz
        order = Order.objects.create(**validated_data)

        total_price = 0
        for item in items_data:
            medicine = item['medicine']
            quantity = item['quantity']

            # Omborda yetarlicha dori borligini tekshirish
            if medicine.stock < quantity:
                raise serializers.ValidationError(
                    f"{medicine.name} dan omborda yetarli emas. Qoldiq: {medicine.stock}"
                )

            # Ombordan dorini ayirib tashlash va saqlash
            medicine.stock -= quantity
            medicine.save()

            # Umumiy narxni hisoblash
            total_price += medicine.price * quantity

            # OrderItem yaratish
            OrderItem.objects.create(order=order, medicine=medicine, quantity=quantity)

        # Hisoblangan umumiy narxni buyurtmaga yozib qoyish
        order.total_price = total_price
        order.save()

        return order