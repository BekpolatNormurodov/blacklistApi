from rest_framework import serializers
from .models import Users, Phones, Cards

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('name', 'surname', 'fatherName', 'birthday', 'isCourt', 'isCar', 'about', 'passportNumber', 'idNumber')

class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = ('number', 'userId')

class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ('bank', 'phone', 'number', 'date', 'fullname', 'userId')