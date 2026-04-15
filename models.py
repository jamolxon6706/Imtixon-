from django.db import models
from django.db.models import Model, CharField, ForeignKey, CASCADE, DecimalField, TextField, TextChoices


class Category(Model):
    name = CharField(max_length=100)

    class Meta:
        db_table = 'category'

class Medicine(Model):
    name = CharField(max_length=255)
    category = ForeignKey(Category,on_delete=CASCADE)
    description = TextField()
    price = DecimalField(max_digits=10, decimal_places=0)
    stock = DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        db_table = 'medicine'

class Country(Model):
    name = CharField(max_length=255)

class City(Model):
    name = CharField(max_length=255)
    country = ForeignKey(Country,on_delete=CASCADE)

    class Meta:
        db_table = 'city'

class Supplier(Model):
    name = CharField(max_length=255)
    phone = CharField(max_length=255)
    city = ForeignKey(City,on_delete=CASCADE)

    class Meta:
        db_table = 'supplier'


class Order(Model):
    class Status(TextChoices):
        A = 'accepted', 'Accepted'
        P = 'process',  'Process'
        D = 'delivered', 'Delivered'
    username = CharField(max_length=255)
    status = CharField(choices=Status, default=Status.A, max_length=20)

class OrderItem(Model):
    order = ForeignKey(Order,on_delete=CASCADE)
    product = ForeignKey(Medicine,on_delete=CASCADE)