from django.shortcuts import render
# from django.http import HttpResponse
import ipdb
from stores.models import Store
from transactions.forms import FileForm
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer
from utils.get_store_balance import get_store_balance

from utils.handleFile import handle_uploaded_file


def upload_file(request):
    if request.method == 'POST':
        # ipdb.set_trace()
        uploaded_file = request.FILES['cnab-file']

        handle_uploaded_file(uploaded_file)

        return render(request, "success.html", {})

    # form = FileForm()
    return render(request, 'upload.html', {})


def list_transactions_by_store(request, store_name):
    store = Store.objects.get(name=store_name.upper())
    transactions = Transaction.objects.filter(store=store)
    serializer = TransactionSerializer(transactions, many=True)

    balance = get_store_balance(serializer.data)
    
    context = {
        "transactions" : serializer.data,
        "store" : store,
        "balance" : balance
    }

    return render(request, "transactions_list.html", context)


def filter_stores(request):

    if request.method == "POST":
        search = request.POST['search-bar']
        # ipdb.set_trace()
        stores = Store.objects.filter(name__icontains=search.upper())
        return render(request, "search_results.html", {'stores': stores})
    
    return render(request, "search_results.html", {})