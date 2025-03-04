from django.db import models


class Address(models.Model):
    address = models.fields.CharField(max_length=100)
    zipCode = models.fields.CharField(max_length=100)
    city = models.fields.CharField(max_length=100)
    email= models.fields.CharField(max_length=100, unique=True)


class Order(models.Model):
    id = models.fields.CharField(max_length=100, primary_key=True, editable=False)
    marketplace = models.fields.CharField(max_length=100)
    date = models.fields.DateField(blank=True, null=True)
    amount = models.fields.FloatField()
    currency = models.fields.CharField(max_length=3)
    billing_adress = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
