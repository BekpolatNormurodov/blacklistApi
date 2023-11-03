from django.contrib import admin
from . models import Users, Phones, Cards, Friends

admin.site.register(Users)
admin.site.register(Phones)
admin.site.register(Cards)
admin.site.register(Friends)