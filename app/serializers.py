from rest_framework import serializers
from .models import Transaction, Manifest, PaymentMethods, Values



# This is a serializer class in Python that defines fields for creating a transaction, including a
# list of values, an external ID, a callback URL, and an amount.
class CreateTransaccionSerializer(serializers.Serializer):
    values = serializers.ListField(child=serializers.CharField())
    external_id = serializers.CharField()
    callback_url = serializers.URLField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)


# This is a Django REST Framework serializer class for the Manifest model that includes all fields.
class ManifestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manifest
        fields = "__all__"


# This is a serializer class for the PaymentMethods model that includes all fields.
class PaymentMethodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethods
        fields = "__all__"


# This is a serializer class for the Values model that includes all fields.
class ValuesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Values
        fields = "__all__"



# The TransactionSerializer class serializes and deserializes Transaction objects, including a nested
# Values object, and overrides the create method to handle creating both objects.
class TransactionSerializer(serializers.ModelSerializer):
    values = ValuesSerializer()

    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self, validated_data):
        values_data = validated_data.pop('values')
        values = Values.objects.create(**values_data)
        transaction = Transaction.objects.create(values=values, **validated_data)
        return transaction

