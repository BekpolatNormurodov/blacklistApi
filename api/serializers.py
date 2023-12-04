from rest_framework import serializers
from .models import Users, Phones, Cards, Friends, Workers
from django.conf import settings

class UsersSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Users
        fields = ('id', 'image','image_url', 'name', 'surname', 'fatherName', 'birthday', 'isCourt', 'isCar', 'about', 'passportNumber', 'idNumber', 'username')

    def get_image_url(self, obj):
        if obj.image:
            image_url = f"{settings.MEDIA_URL}{obj.image}"
            modified_url = f"{settings.BASE_URL}/blacklistApi{image_url}"
            return modified_url
        return None




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

class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = ('id', 'username', 'admin')