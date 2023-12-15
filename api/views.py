from rest_framework.response import Response
from .models import *
from .serializers import  *
from rest_framework.generics import *
from rest_framework.views import APIView

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


# WORKERS
class WorkersView(ListAPIView):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer

class WorkersCreate(ListCreateAPIView):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer

class WorkersUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer




class SearchApiView(APIView):
    serializer_class = UsersSerializer
    serializer_class = PhonesSerializer
    serializer_class = CardsSerializer
    def get(self, request):
        users = Users.objects.all().values()
        phones = Phones.objects.all().values()
        cards = Cards.objects.all().values()
        data = [
           users,
           cards,
           phones
        ]
        return Response(data)