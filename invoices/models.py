from django.db import models


class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    business_name = models.CharField(max_length=100)
    business_email = models.EmailField()
    business_address = models.CharField(max_length=100)

    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    client_address = models.CharField(max_length=100)

    invoice_number = models.CharField(max_length=100)
    invoice_date = models.DateField()
    invoice_due_date = models.DateField()
    invoice_description = models.CharField(max_length=100)
    invoice_logo = models.ImageField()


class InvoiceItem(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    unit_price = models.FloatField(default=0)
    details = models.TextField(max_length=300)

    def subtotal(self):
        total = (self.quantity * self.unit_price)
        return total
