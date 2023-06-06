from django.contrib import admin
from django.urls import path
from .views import InvoiceListView, createInvoice, generate_pdf, view_PDF

app_name = 'invoice'
urlpatterns = [
    path('list/', InvoiceListView.as_view(), name="invoice-list"),
    path('create/', createInvoice, name="invoice-create"),
    path('invoice-detail/<id>', view_PDF, name='invoice-detail'),
    path('invoice-download/<id>', generate_pdf, name='invoice-download')
   
]
