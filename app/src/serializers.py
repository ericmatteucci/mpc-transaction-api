from app.src.models import Transaction, User
from rest_framework import serializers


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['username', 'date', 'description', 'paid_out', 'paid_in', 'balance', 'category', 'notes']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']