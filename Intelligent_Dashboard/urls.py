"""Intelligent_Dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from authentication import views as auth_views
from pdf_form import  views as pdf_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pdf_form.urls")),
    path('', include('authentication.urls')),
    path('create/', pdf_views.createInvoice, name="invoice-create"),
    path('list/', pdf_views.InvoiceListView.as_view(), name="invoice-list"),
    path('invoice-detail/', pdf_views.view_PDF, name='invoice-detail'),
    path('invoice-download/<id>', pdf_views.generate_pdf, name='invoice-download'),
    path('update/<id>/', pdf_views.update_data, name="update"),
    path('sign/<id>/', pdf_views.sign, name="sign")
]
