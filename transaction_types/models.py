from django.db import models    
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

class Description(models.TextChoices):
    DEBITO = "Debito"
    BOLETO = "Boleto"
    FINANCIAMENTO = "Financiamento"
    CREDITO = "Credito"
    RECEBIMENTO_EMPRESTIMO = "Recebimento Emprestimo"
    VENDAS="Vendas"
    RECEBIMENTO_TED="Recebimento TED"
    RECEBIMENTO_DOC="Recebimento DOC"
    ALUGUEL="Aluguel"
    DEFAULT="Não Informado"

class Nature(models.TextChoices):
    ENTRADA = "Entrada"
    SAIDA = "Saida"
    DEFAULT = "Não Informado"

class TransactionType(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type= models.IntegerField(validators=[MaxValueValidator(9), MinValueValidator(1)], unique=True)
    description = models.CharField(max_length=22, unique=True, choices=Description.choices, default=Description.DEFAULT)
    nature = models.CharField(max_length=13, choices=Nature.choices, default=Nature.DEFAULT)

