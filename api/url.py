from django.urls import path
from .views import UsersView, UsersCreate, UsersUpdate, PhonesView, PhonesCreate, PhonesUpdate

urlpatterns = [
    # Users
    path('users/',UsersView.as_view()),
    path('users/post/',UsersCreate.as_view()),
    path('users/<int:pk>',UsersUpdate.as_view()),
    
    # Phones
    path('phones/',PhonesView.as_view()),
    path('phones/post/',PhonesCreate.as_view()),
    path('phones/<int:pk>',PhonesUpdate.as_view()),
]