from django.db import models
from django.forms import CharField, IntegerField

class Payment(models.Model):
    external_id = models.CharField(max_length=255)
    callback_url = models.URLField()
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
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.external_id
