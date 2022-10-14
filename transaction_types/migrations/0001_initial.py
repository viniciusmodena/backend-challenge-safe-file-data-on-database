# Generated by Django 4.1.1 on 2022-10-13 04:55

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TransactionType",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "type",
                    models.IntegerField(
                        unique=True,
                        validators=[
                            django.core.validators.MaxValueValidator(9),
                            django.core.validators.MinValueValidator(1),
                        ],
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        choices=[
                            ("Debito", "Debito"),
                            ("Boleto", "Boleto"),
                            ("Financiamento", "Financiamento"),
                            ("Credito", "Credito"),
                            ("Recebimento Emprestimo", "Recebimento Emprestimo"),
                            ("Vendas", "Vendas"),
                            ("Recebimento TED", "Recebimento Ted"),
                            ("Recebimento DOC", "Recebimento Doc"),
                            ("Aluguel", "Aluguel"),
                            ("Não Informado", "Default"),
                        ],
                        default="Não Informado",
                        max_length=22,
                        unique=True,
                    ),
                ),
                (
                    "nature",
                    models.CharField(
                        choices=[
                            ("Entrada", "Entrada"),
                            ("Saida", "Saida"),
                            ("Não Informado", "Default"),
                        ],
                        default="Não Informado",
                        max_length=13,
                    ),
                ),
            ],
        ),
    ]
