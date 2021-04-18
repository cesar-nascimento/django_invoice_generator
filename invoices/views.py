from django.shortcuts import render
from invoices.forms import InvoiceForm, InvoiceItemForm
from django.forms import formset_factory


def index(request):
    invoice_form = InvoiceForm()
    invoice_item_formset = formset_factory(InvoiceItemForm)

    context = {
        'invoice_form': invoice_form,
        'invoice_item_formset': invoice_item_formset
    }

    return render(request, 'index.html', context)


def invoice(request):
    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST)

        InvoiceItemFormset = formset_factory(InvoiceItemForm)

        invoice_item_formset = InvoiceItemFormset(request.POST)

        context = {
            'invoice_form': invoice_form,
            'invoice_item_formset': invoice_item_formset,
        }

        return render(request, 'invoice.html', context)
