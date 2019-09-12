from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Transaction(models.Model):
    date = models.DateField
    description = models.CharField(max_length=100)
    paid_out = models.DecimalField(decimal_places=2)
    paid_in = models.DecimalField(decimal_places=2)
    balance = models.DecimalField(decimal_places=2)
    category = models.CharField(max_length=30)
    notes = models.CharField(max_length=100)
    