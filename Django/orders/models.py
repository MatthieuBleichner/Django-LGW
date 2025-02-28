from django.db import models

class Order(models.Model):
    marketplace = models.fields.CharField(max_length=100)
    ref_id = models.fields.CharField(max_length=100, primary_key=True, editable=False)
    date = models.fields.DateField(blank=True, null=True)
    amount = models.fields.DecimalField(max_digits=10, decimal_places=2)
    currency = models.fields.CharField(max_length=3)

