from .models import Users, Phones
from .serializers import UsersSerializer, PhonesSerializer
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