from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    fatherName = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name[:20]

class Phones(models.Model):
    number = models.IntegerField(null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.number[:20]