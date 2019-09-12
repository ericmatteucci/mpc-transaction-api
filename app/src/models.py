from django.db import models


class Transaction(models.Model):
    username = models.CharField(max_length=50)
    date = models.DateField
    description = models.CharField(max_length=100)
    paid_out = models.DecimalField(max_digits=15, decimal_places=2)
    paid_in = models.DecimalField(max_digits=15, decimal_places=2)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.CharField(max_length=30)
    notes = models.CharField(max_length=100)


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)