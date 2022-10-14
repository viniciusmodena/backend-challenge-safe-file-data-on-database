from rest_framework import generics
from transaction_types.models import TransactionType
from transaction_types.serializers import TransactionTypesSerializers

class TransactionTypesView(generics.ListAPIView):
    queryset = TransactionType.objects.all()
    serializer_class = TransactionTypesSerializers