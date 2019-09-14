import csv, io, datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from app.src.models import Transaction


def generate_csv(request):
    """
    Creates a csv of all of the transactions for a particular user.
    :param request: The CSV download request.
    :return: The generated CSV file for the particular user.
    """

    # get all of the data for the particular user
    queryset = Transaction.objects.filter(username=request.user.username).all().order_by('-date')

    # generate the response and set the file name as <username>_transactions.csv
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + request.user.username + '_transactions.csv'

    # write the headers for the csv output file
    csv_writer = csv.writer(response, delimiter=',')
    csv_writer.writerow(['Date', 'Description', 'Paid Out', 'Paid In', 'Balance', 'Category', 'Notes'])

    # generate the data rows for the csv output file
    for result in queryset:
        csv_writer.writerow([
            result.date,
            result.description,
            result.paid_out,
            result.paid_in,
            result.balance,
            result.category,
            result.notes,
        ])

    return response


@login_required(login_url='/api-auth/login/')
def list_transactions(request):
    """
    Creates a multi-function view, listing transactions for the currently logged in user. Also allows the
    user to filter by category and download the transactions to a csv file.
    :param request: The incoming request
    :return: Updates the view appropriately, listing the data and/or downloading the CSV file.
    """
    list_template = 'list_transactions.html'
    queryset = None

    if request.method == 'GET' or request.POST.get('show_all'):
        queryset = Transaction.objects.filter(
            username=request.user.username).all().order_by('-date')
    elif request.POST.get('category_submit'):
        queryset = Transaction.objects.filter(
            username=request.user.username, category=request.POST.get('category')).order_by('-date')
    elif request.POST.get('download'):
        return generate_csv(request)
    else:
        messages.error(request, 'INVALID REQUEST: Please reload and try again.')

    params = {
        'transactions': queryset,
        'username': request.user.username,
    }

    return render(request, list_template, params)


@login_required(login_url='/api-auth/login/')
def upload_transactions(request):
    """
        Creates a view where the user can upload a CSV to the database. Parses the CSV and saves it
        in the DB.
    :param request: The request containing the CSV file to upload.
    :return:
    """
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
