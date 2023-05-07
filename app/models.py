from django.db import models
from django.forms import CharField, IntegerField


# This is a Django model class with various fields for storing values related to a merchant's
# information and transaction details.
class Values(models.Model):
    merchant_id = models.CharField(max_length=255)
    submerchant_id = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    ruc = models.CharField(max_length=255)
    currency = models.CharField(max_length=3)
    document_number = models.CharField(max_length=255)
    document_type = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    country_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    payment_concept = models.CharField(max_length=255)
    shipping_postal_code = models.CharField(max_length=10)
    shipping_address = models.CharField(max_length=255)
    additional_data1 = models.CharField(max_length=255)
    additional_data2 = models.CharField(max_length=255)

    def __str__(self):
        return self.merchant_id


# The Transaction class defines a model with fields for an external ID, callback URL, a foreign key to
# a Values model, and an amount.
class Transaction(models.Model):
    external_id = models.CharField(max_length=255)
    callback_url = models.URLField()
    values = models.ForeignKey(Values, on_delete=models.CASCADE, related_name='values')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.external_id


# This is a Django model class called Manifest with two fields: name and allowsSplit.
class Manifest(models.Model):
    name = models.CharField(max_length=255)
    allowsSplit =  models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

# This is a Django model class for PaymentMethods with a single field for payment method name.
class PaymentMethods(models.Model):
    paymentMethods = models.CharField(max_length=255)

    def __str__(self):
        return self.paymentMethods