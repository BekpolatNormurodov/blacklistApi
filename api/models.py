from django.db import models

class Users(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    fatherName = models.CharField(max_length=100, null=True)
    birthday = models.CharField(max_length=100, null=True)
    isCourt = models.CharField(max_length=10, null=True)
    isCar = models.CharField(max_length=10, null=True)
    about = models.TextField(max_length=10000, null=True)
    passportNumber= models.CharField(max_length=100, null=True)
    idNumber = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name[:20]

class Phones(models.Model):
    number = models.CharField(max_length=100 ,null=True)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.number[:20]
    
class Cards(models.Model):
    bank = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=100, null=True)
    date = models.CharField(max_length=100, null=True)
    fullname = models.CharField(max_length=100, null=True)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.number[:20]
    
class Friends(models.Model):
    image = models.CharField(max_length=100, null=True)
    fullname = models.CharField(max_length=100, null=True)
    index = models.IntegerField(null=True)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.fullname[:20]
    
class Workers(models.Model):
    username = models.CharField(max_length=100, null=True)
    admin = models.BooleanField(null=True)

    def __str__(self):
        return self.username[:20]