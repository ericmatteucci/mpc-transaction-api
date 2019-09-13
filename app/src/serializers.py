from app.src.models import Transaction, User
from rest_framework import serializers


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'username', 'date', 'description', 'paid_out', 'paid_in', 'balance', 'category', 'notes']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']