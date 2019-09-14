import csv, io, datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app.src.models import Transaction


@login_required(login_url='/api-auth/login/')
def list_transactions(request):
    list_template = 'list_transactions.html'

    if request.method == 'GET' or request.POST.get('show_all'):
        queryset = Transaction.objects.filter(
            username=request.user.username).all().order_by('-date')
    elif request.POST.get('category_submit'):
        queryset = Transaction.objects.filter(
            username=request.user.username, category=request.POST.get('category')).order_by('-date')

    params = {
        'transactions': queryset,
        'username': request.user.username,
    }

    return render(request, list_template, params)


@login_required(login_url='/api-auth/login/')
def upload_transactions(request):
    upload_template = 'transaction_upload.html'

    if request.method == 'GET' or 'file' not in request.FILES:
        prompt = {
            'message': 'Upload a transactions CSV file.',
        }
        return render(request, upload_template, prompt)

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
            username=request.user.username,
            date=datetime.datetime.strptime(col[0], '%d %b %Y'),
            description=col[1],
            paid_out=paid_out_val,
            paid_in=paid_in_val,
            balance=col[4],
            category=col[5],
            notes=col[6]
        )

    return render(request, upload_template, {})
