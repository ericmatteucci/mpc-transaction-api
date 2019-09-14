from app.src.models import Transaction
from rest_framework import serializers


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'username', 'date', 'description', 'paid_out', 'paid_in', 'balance', 'category', 'notes']
