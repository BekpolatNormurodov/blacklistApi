from django.urls import path
from .views import SearchUsersView,SearchUsersCreate, SearchUsersUpdate, UsersView, UsersCreate, UsersUpdate, PhonesView, PhonesCreate, PhonesUpdate, CardsView, CardsCreate, CardsUpdate, FriendsView, FriendsCreate, FriendsUpdate

urlpatterns = [
    # SearchUsers
    path('searchusers/',SearchUsersView.as_view()),
    path('searchusers/post/',SearchUsersCreate.as_view()),
    path('searchusers/<int:pk>',SearchUsersUpdate.as_view()),

     # Users
    path('users/',UsersView.as_view()),
    path('users/post/',UsersCreate.as_view()),
    path('users/<int:pk>',UsersUpdate.as_view()),

    # Phones
    path('phones/',PhonesView.as_view()),
    path('phones/post/',PhonesCreate.as_view()),
    path('phones/<int:pk>',PhonesUpdate.as_view()),

    # Cards
    path('cards/',CardsView.as_view()),
    path('cards/post/',CardsCreate.as_view()),
    path('cards/<int:pk>',CardsUpdate.as_view()),

    # Friends
    path('friends/',FriendsView.as_view()),
    path('friends/post/',FriendsCreate.as_view()),
    path('friends/<int:pk>',FriendsUpdate.as_view()),
]