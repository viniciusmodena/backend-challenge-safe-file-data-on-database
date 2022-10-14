from django.db import models
import uuid

class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    
    date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    cpf = models.CharField(max_length=11)
    card_number = models.CharField(max_length=12)
    time = models.TimeField()

    type = models.ForeignKey("transaction_types.TransactionType", on_delete=models.CASCADE, related_name="transations") 
    store = models.ForeignKey("stores.Store", on_delete=models.CASCADE, related_name="transactions")
