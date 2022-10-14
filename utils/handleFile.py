import datetime
from django.shortcuts import get_object_or_404

from stores.models import Store
from transaction_types.models import TransactionType
from transactions.models import Transaction


def parseDate(date_string):
    year = int(date_string[0:4])
    month = int(date_string[4:6])
    day = int(date_string[6:8])

    return datetime.date(year, month, day)


def parseTime(time_string):
    hour = int(time_string[0:2])
    minutes = int(time_string[2:4])
    seconds = int(time_string[4:6])

    return datetime.time(hour,minutes,seconds)


def parseStoreOwner(store_owner_string):
    return store_owner_string.rstrip()


def parseStoreName(store_name_string):
    return store_name_string.replace("\n", "").rstrip().upper()


def registerTransaction(store_owner, store_name, type, transaction_data):
    transaction_type = get_object_or_404(TransactionType, type=type)
    store, _ = Store.objects.get_or_create(name=store_name, owner=store_owner)

    if not Transaction.objects.filter(**transaction_data, store=store, type=transaction_type).exists():
        Transaction.objects.create(**transaction_data, store=store, type=transaction_type)



def handle_uploaded_file(file):
    for line in file:
        decoded_line = line.decode('utf-8')

        type = decoded_line[0:1]
        date = parseDate(decoded_line[1:9])
        amount = decoded_line[9:19]
        cpf = decoded_line[19:30]
        card_number = decoded_line[30:42]
        time = parseTime(decoded_line[42:48])
        store_owner = parseStoreOwner(decoded_line[48:62])
        store_name = parseStoreName(decoded_line[62:81])

        transaction_data={
            "date" : date,
            "amount" : amount,
            "cpf" : cpf,
            "card_number" : card_number,
            "time" : time,
        }

        registerTransaction(store_owner, store_name, type, transaction_data)

