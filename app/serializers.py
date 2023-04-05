from rest_framework import serializers
from .models import Payment


class MerchantValuesSerializer(serializers.Serializer):
    merchant_id = serializers.CharField(max_length=100)
    submerchant_id = serializers.CharField(max_length=100)
    company_name = serializers.CharField(max_length=100)
    ruc = serializers.CharField(max_length=100)
    currency = serializers.CharField(max_length=100)
    document_number = serializers.CharField(max_length=100)
    document_type = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    country_code = serializers.CharField(max_length=10)
    phone_number = serializers.CharField(max_length=15)
    payment_concept = serializers.CharField()
    shipping_postal_code = serializers.CharField(max_length=10)
    shipping_address = serializers.CharField()
    additional_data1 = serializers.CharField(max_length=100)
    additional_data2 = serializers.CharField(max_length=100)

class PaymentSerializer(serializers.Serializer):
    external_id = serializers.CharField(max_length=100)
    callback_url = serializers.URLField()
    values = MerchantValuesSerializer()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        values_data = validated_data.pop('values')
        values = values.objects.create(**values_data)
        validated_data['values'] = values
        return Payment.objects.create(**validated_data)
