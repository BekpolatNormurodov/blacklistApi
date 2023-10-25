from rest_framework import serializers
from .models import Users, Phones

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name', 'surname', 'fatherName', 'age', 'isCourt', 'isCar', 'about', 'passportNumber', 'idNumber')

class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = ('id', 'number', 'user')