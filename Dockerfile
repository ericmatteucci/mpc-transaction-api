FROM django

ADD . /mpc-transactions-api

WORKDIR /mpc-transactions-api

RUN pip install -r requirements.txt

CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]