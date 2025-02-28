from django.db import models

class Order(models.Model):
    id = models.fields.CharField(max_length=100, primary_key=True, editable=False)
    marketplace = models.fields.CharField(max_length=100)
    date = models.fields.DateField(blank=True, null=True)
    amount = models.fields.FloatField()
    currency = models.fields.CharField(max_length=3)

