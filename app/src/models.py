from django.db import models
from django.utils import timezone


class Transaction(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    username = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    description = models.CharField(max_length=100)
    paid_out = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    paid_in = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.CharField(max_length=30)
    notes = models.CharField(max_length=100, null=True)
