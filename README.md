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
