import ipdb

from utils.get_currency import get_currency

def get_store_balance(transactions_list):
    balance=0
    
    for transaction in transactions_list:
        # ipdb.set_trace()
        if transaction["type"]["nature"] == "Entrada":
            balance += float(transaction["amount"])
        elif transaction["type"]["nature"] == "Saida":
            balance -= float(transaction["amount"])

    return get_currency(balance)

