from asyncore import read
from rest_framework import serializers
from stores.serializer import StoreSerializer
from transaction_types.serializers import TransactionTypesSerializers

from transactions.models import Transaction
from utils.get_currency import get_currency

import ipdb

class TransactionSerializer(serializers.ModelSerializer):
    store = StoreSerializer(read_only=True)
    type = TransactionTypesSerializers(read_only=True)
    value = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Transaction
        fields = "__all__"

    def get_value(self, obj):
        return get_currency(obj.amount)