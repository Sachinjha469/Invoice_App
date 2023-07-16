from django.db import models


class Invoice(models.Model):
    customer = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    total_quantity = models.IntegerField(default=0)
    total_amount = models.FloatField(default=0.0)


class Transaction(models.Model):
    product = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    line_total = models.FloatField(default=0.0)
    invoice_id = models.ForeignKey(Invoice, related_name="user_transaction", on_delete=models.CASCADE)

