from invoices.models import InvoiceItem, Invoice
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, TextInput, EmailInput, ClearableFileInput, NumberInput, Textarea
from tempus_dominus.widgets import DatePicker
from datetime import datetime


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

        labels = {
            'business_name': _('Name:'),
            'business_email': _('Email:'),
            'business_address': _('Address:'),

            'client_name': _('Name:'),
            'client_email': _('Email:'),
            'client_address': _('Address:'),

            'invoice_number': _('Number:'),
            'invoice_date': _('Date:'),
            'invoice_due_date': _('Due date:'),
            'invoice_description': _('Description:'),
        }
        widgets = {
            'business_name': TextInput(attrs={'placeholder': 'Business name'}),
            'business_email': EmailInput(attrs={'placeholder': 'your@email.com'}),
            'business_address': TextInput(attrs={'placeholder': 'Your address'}),

            'client_name': TextInput(attrs={'placeholder': 'Client name'}),
            'client_email': EmailInput(attrs={'placeholder': 'client@email.com'}),
            'client_address': TextInput(attrs={'placeholder': 'Client address'}),

            'invoice_logo': ClearableFileInput(),
            'invoice_number': TextInput(attrs={'placeholder': 'ABC#1234'}),
            'invoice_date': DatePicker(),
            'invoice_due_date': DatePicker(),
            'invoice_description': TextInput(attrs={'placeholder': 'Invoice'}),
        }



class InvoiceItemForm(ModelForm):
    class Meta:
        model = InvoiceItem
        fields = '__all__'

        widgets = {
            'description': TextInput(attrs={'placeholder': 'Item name'}),
            'details': Textarea(attrs={'placeholder': 'Item description'}),
            'quantity': NumberInput(attrs={'placeholder': '1'}),
            'unit_price': NumberInput(attrs={'placeholder': '1.00', 'step': "0.01"}),
        }
