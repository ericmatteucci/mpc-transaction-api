# MPC Example - Transactions API
#### Eric Matteucci

Welcome to my example solution for the Transactions API. Please find some startup information below.

## Installing
It is recommended that a virtual environment be set up to run this application.
Within the virtual environment, you can set up the project dependencies by running the following:
```shell script
$ pip install --upgrade -r requirements.txt --user
```
_Note that this set up is for a system running Windows 10. Installation may differ between
operating systems._

## Creating Users
Since only registered users that have been added by the company can use the application,
we need a way to add new users. Do this with the following command:
```shell script
python manage.py createsuperuser --email <email_example@example.com> --username <username_example>
```
You will be prompted to add a password after the commands execution.

## Running the application
To run, first the DB needs to be built by making and running a migration. This can be done with the
following commands:
```shell script
python manage.py makemigrations
python manage.py migrate
```
Once the commands execute, you can start the server. Do this with the following:
```shell script
python manage.py runserver
```

## Using the API
The API has been programmed with two endpoints. One for uploading data and one for viewing and downloading data.
Note that you MUST be logged in before using either of the endpoints. Accessing either will redirect you
to the login page. Your user needs to be created in order to log in. (See 'Installing' above for creating
users.) The endpoints are listed below:
```text
http://127.0.0.1:8000/list/
http://127.0.0.1:8000/upload/
```

The list endpoint allows you to view all of the transactions for the currently logged in user. It also
allows you to sort the results by category. Press 'show all' to clear the search criteria. Finally, you can
download all of your transaction data by pressing 'download'.

