from rest_framework import serializers
from .models import SearchUsers, Users, Phones, Cards, Friends

class SearchUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchUsers
        fields = ('id', 'username')

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
        fields = ('id', 'name', 'userId')