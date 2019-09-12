from rest_framework import viewsets
from app.src.models import Transaction, User
from app.src.serializers import TransactionSerializer, UserSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer