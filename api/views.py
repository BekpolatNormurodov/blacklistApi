from .models import Users, Phones,Cards, Friends
from .serializers import UsersSerializer, PhonesSerializer, CardsSerializer, FriendsSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

# USERS
class UsersView(ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UsersCreate(ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UsersUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

# PHONES
class PhonesView(ListAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer

class PhonesCreate(ListCreateAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer

class PhonesUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer

# CARDS
class CardsView(ListAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer

class CardsCreate(ListCreateAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer

class CardsUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer


# FRIENDS
class FriendsView(ListAPIView):
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer

class FriendsCreate(ListCreateAPIView):
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer

class FriendsUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer