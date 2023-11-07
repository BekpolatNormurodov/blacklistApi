from rest_framework import serializers
from .models import Users, Phones, Cards, Friends

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name', 'surname', 'fatherName', 'birthday', 'isCourt', 'isCar', 'about', 'passportNumber', 'idNumber')

class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = ('id', 'number', 'userId')

class CardsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Cards
        fields = ('id', 'bank', 'phone', 'number', 'date', 'fullname', 'userId')

class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ('id', 'fullname', 'index', 'userId')