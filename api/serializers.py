from rest_framework import serializers
from .models import *
from django.conf import settings

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name', 'surname', 'username', 'birthday', 'passport_number', 'id_number')


class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = ('id', 'number', 'user')

class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ('id', 'bank', 'number', 'expiry_date', 'user')

class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ('id', 'fullname', 'user')

class PhonesDetailSerializer(serializers.ModelSerializer):
    user = UsersSerializer(read_only=True)
    cards = serializers.SerializerMethodField()
    
    class Meta:
        model = Phones
        fields = ('id', 'number', 'user', 'cards')
    
    def get_cards(self, obj):
        cards = Cards.objects.filter(user=obj.user)
        return CardsSerializer(cards, many=True).data

class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = ('id', 'username', 'admin')
