from rest_framework import serializers

from transaction_types.models import TransactionType

class TransactionTypesSerializers(serializers.ModelSerializer):
    sign = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TransactionType
        fields = "__all__"

    def get_sign(self, obj):
        if obj.nature == "Entrada":
            return "+"
        
        return "-"