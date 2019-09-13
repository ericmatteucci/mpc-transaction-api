import csv, io, datetime
from django.contrib import messages
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from app.src.models import Transaction, User
from app.src.serializers import TransactionSerializer, UserSerializer


class TransactionViewSet(viewsets.ViewSet):
    """
        Use this endpoint to view all of the transactions in the system.
    """

    def list(self, request):
        queryset = Transaction.objects.all()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    """
        Use this endpoint to view all of the users saved to the system.
    """
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer


def upload_transactions(request):
    template = 'transaction_upload.html'

    prompt = {
        'message': 'Upload a transactions CSV file.',
    }

    if request.method == 'GET' or 'file' not in request.FILES:
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'File is not of proper format. Please upload a CSV file.')

    data = csv_file.read().decode('UTF-8')
    data_string = io.StringIO(data)

    # skip the header line
    next(data_string)

    for col in csv.reader(data_string, delimiter=','):
        paid_out_val = col[2] if col[2] != '' else 0
        paid_in_val = col[3] if col[3] != '' else 0

        _, row = Transaction.objects.update_or_create(
            date=datetime.datetime.strptime(col[0], '%d %b %Y'),
            description=col[1],
            paid_out=paid_out_val,
            paid_in=paid_in_val,
            balance=col[4],
            category=col[5],
            notes=col[6]
        )

    return render(request, template, {})
