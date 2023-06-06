from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.template.loader import get_template
from django.http import HttpResponse
from django.views import View
from .models import *
from .forms import *
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required

import pdfkit


class InvoiceListView(View):
    def get(self, *args, **kwargs):
        invoices = Invoice.objects.all()
        context = {
            "invoices":invoices,
        }

        return render(self.request, 'pdf_form/invoice-list2.html', context)
    
    def post(self, request):        
        # import pdb;pdb.set_trace()
        invoice_ids = request.POST.getlist("invoice_id")
        invoice_ids = list(map(int, invoice_ids))

        update_status_for_invoices = int(request.POST['status'])
        invoices = Invoice.objects.filter(id__in=invoice_ids)
        # import pdb;pdb.set_trace()
        if update_status_for_invoices == 0:
            invoices.update(status=False)
        else:
            invoices.update(status=True)

        return redirect('invoice:invoice-list')

@login_required
def createInvoice(request):
    if request.method == 'GET':
        formset1 = LineItemFormset(request.GET or None)
        formset2 = LampiranCFormset(request.GET or None)
        formset3 = LampiranC2Formset(request.GET or None)
        formset4 = LampiranDFormset(request.GET or None)
        formset5 = pengarahFormset(request.GET or None)
        formset6 = timbalanFormset(request.GET or None)

        form = InvoiceForm(request.GET or None)
    elif request.method == 'POST':
        formset1 = LineItemFormset(request.POST)
        formset2 = LampiranCFormset(request.POST)
        formset3 = LampiranC2Formset(request.POST)
        formset4 = LampiranDFormset(request.POST)
        formset5 = pengarahFormset(request.POST)
        formset6 = timbalanFormset(request.POST)
        form = InvoiceForm(request.POST)
        
        if form.is_valid():
            invoice = Invoice.objects.create(
                                            TITLE=form.data["TITLE"],
                                            TARIKH=form.data["TARIKH"],
                                            MASA=form.data["MASA"],
                                            TEMPAT=form.data["TEMPAT"],
                                            ANJURAN=form.data["ANJURAN"],
                                            TUJUAN=form.data["TUJUAN"],
                                            LATAR_BELAKANG=form.data["LATAR_BELAKANG"],
                                            Objektif_1=form.data["Objektif_1"],  
                                            Tarikh_A=form.data["Tarikh_A"],
                                            Tempat_A=form.data["Tempat_A"],
                                            Sasaran_peserta=form.data["Sasaran_peserta"],
                                            Jawatankuasa_Pelaksana=form.data["Jawatankuasa_Pelaksana"],
                                            Atur_Cara=form.data["Atur_Cara"],
                                            Implikasi_Kewangan=form.data["Implikasi_Kewangan"],
                                            SETIAUSAHA=form.data["SETIAUSAHA"],
                                            BENDAHARI=form.data["BENDAHARI"],
                                            JAWATANKUASA_PERALATAN_DAN_TEKNIKAL=form.data["JAWATANKUASA_PERALATAN_DAN_TEKNIKAL"],
                                            JAWATANKUASA_JEMPUTAN=form.data["JAWATANKUASA_JEMPUTAN"],
                                            JAWATANKUASA_AKTIVITI=form.data["JAWATANKUASA_AKTIVITI"],
                                            Atur_Cara_B=form.data["Atur_Cara_B"],
                                            Tarikh_B=form.data["Tarikh_B"],
                                            Masa_B=form.data["Masa_B"],
                                            Tempat_B=form.data["Tempat_B"],
                                            Name_1=form.data["Name_1"],
                                            )
            # invoice.save()
            user =  request.user
            invoice.user = user


        if formset1.is_valid():
            
            for form in formset1:
                Masa_B1 = form.cleaned_data.get('Masa_B1')
                activity_B1 = form.cleaned_data.get('activity_B1')
                
                
                if Masa_B1 and activity_B1 :
                    
                    
                    LineItem(customer=invoice,
                            Masa_B1=Masa_B1,
                            activity_B1=activity_B1,
                            ).save()
            

        if formset2.is_valid():

            total = 0

            for form in formset2:   
                value_1 = form.cleaned_data.get('value_1')
                Amount_1 = form.cleaned_data.get('Amount_1')  

                if value_1 and Amount_1 :
                    total += Amount_1

                    LampiranC(
                        modelC=invoice,
                        value_1=value_1,
                        Amount_1=Amount_1
                        ).save()

                invoice.JUMLAH_KESELURUHAN_1 = total

        if formset3.is_valid():

            total2 = 0

            for form in formset3:
                value_C1 = form.cleaned_data.get('value_C1')
                Amount_C1 = form.cleaned_data.get('Amount_C1')  

                if value_C1 and Amount_C1 :
                    total2 += Amount_C1

                    LampiranC2(
                        modelC2=invoice,
                        value_C1=value_C1,
                        Amount_C1=Amount_C1
                        ).save()

            invoice.JUMLAH_KESELURUHAN_2 = total2

        if formset4.is_valid():
            # import pdb;pdb.set_trace()
            # extract name and other data from each form and save
            
            for form in formset4:
                field = form.cleaned_data.get('field')
                data = form.cleaned_data.get('data')
                
                
                if field and data :
                    
                    
                    LampiranD(
                            modelD=invoice,
                            field=field,
                            data=data,
                            ).save()
                    
        if formset5.is_valid():
            
            for form in formset5:
                PENGARAH = form.cleaned_data.get('PENGARAH')
                
                if PENGARAH :
                    
                    Pengarah(
                            model1=invoice,
                            PENGARAH=PENGARAH,
                            ).save()
                
            

        if formset6.is_valid():
            
            for form in formset6:
                TIMBALAN_PENGARAH = form.cleaned_data.get('TIMBALAN_PENGARAH')
                
                if TIMBALAN_PENGARAH :
                    
                    Timbalan(
                            model2=invoice,
                            TIMBALAN_PENGARAH=TIMBALAN_PENGARAH,
                            ).save()
                    
                invoice.save()

            return redirect("/list")


            try:
                generate_pdf(request, pk=invoice.id)
            except Exception as e:
                print(f"********{e}********")
        

        
    context = {
        "title" : "form",
        "form": form,
        "formset1": formset1,
        "formset2": formset2,
        "formset3": formset3,
        "formset4": formset4,
        "formset5": formset5,
        "formset6": formset6,
        
    }
    return render(request, 'pdf_form/entry.html', context)    


def view_PDF(request, id=None):
    invoice = get_object_or_404(Invoice, id=id)
    lineitem = invoice.lineitem_set.all()
    lampiranc = invoice.lampiranc_set.all()
    lampiranc2 = invoice.lampiranc2_set.all()
    lampirand = invoice.lampirand_set.all()   
    pengarah = invoice.pengarah_set.all()
    timbalan = invoice.timbalan_set.all()

    

    context = { "invoice_id": invoice.user,
                "TITLE":invoice.TITLE,
                "TARIKH":invoice.TARIKH,
                "MASA":invoice.MASA,
                "TEMPAT":invoice.TEMPAT,
                "ANJURAN":invoice.ANJURAN,
                "TUJUAN":invoice.TUJUAN,
                "LATAR_BELAKANG":invoice.LATAR_BELAKANG,
                "Objektif_1":invoice.Objektif_1,  
                "Tarikh_A":invoice.Tarikh_A,
                "Tempat_A":invoice.Tempat_A,
                "Sasaran_peserta":invoice.Sasaran_peserta,
                "Jawatankuasa_Pelaksana":invoice.Jawatankuasa_Pelaksana,
                "Atur_Cara":invoice.Atur_Cara,
                "Implikasi_Kewangan":invoice.Implikasi_Kewangan,
                "SETIAUSAHA":invoice.SETIAUSAHA,
                "BENDAHARI":invoice.BENDAHARI,
                "JAWATANKUASA_PERALATAN_DAN_TEKNIKAL":invoice.JAWATANKUASA_PERALATAN_DAN_TEKNIKAL,
                "JAWATANKUASA_JEMPUTAN":invoice.JAWATANKUASA_JEMPUTAN,
                "JAWATANKUASA_AKTIVITI":invoice.JAWATANKUASA_AKTIVITI,
                "Tarikh_B":invoice.Tarikh_B,
                "Masa_B":invoice.Masa_B,
                "Tempat_B":invoice.Tempat_B,
                "Name_1":invoice.Name_1,


                "lineitem": lineitem,
                "lampiranc":lampiranc,
                "lampiranc2":lampiranc2,
                "lampirand":lampirand,
                "pengarah":pengarah,
                "timbalan":timbalan,

        }
    return render(request, 'pdf_form/pdf_template.html', context)


def generate_pdf(request,id=None):
    invoice = get_object_or_404(Invoice, id=id)
    lineitem = invoice.lineitem_set.all()
    lampiranc = invoice.lampiranc_set.all()
    lampiranc2 = invoice.lampiranc2_set.all()
    lampirand = invoice.lampirand_set.all()    
    pengarah = invoice.pengarah_set.all()
    timbalan = invoice.timbalan_set.all()


    response = HttpResponse(content_type='pdf_form/pdf1')
    response['Content-Disposition'] = 'filename="note.pdf"'
    template = get_template('pdf_form/pdf1.html')

    context = { "TITLE":invoice.TITLE,
                "TARIKH":invoice.TARIKH,
                "MASA":invoice.MASA,
                "TEMPAT":invoice.TEMPAT,
                "ANJURAN":invoice.ANJURAN,
                "TUJUAN":invoice.TUJUAN,
                "LATAR_BELAKANG":invoice.LATAR_BELAKANG,
                "Objektif_1":invoice.Objektif_1,  
                "Tarikh_A":invoice.Tarikh_A,
                "Tempat_A":invoice.Tempat_A,
                "Sasaran_peserta":invoice.Sasaran_peserta,
                "Jawatankuasa_Pelaksana":invoice.Jawatankuasa_Pelaksana,
                "Atur_Cara":invoice.Atur_Cara,
                "Implikasi_Kewangan":invoice.Implikasi_Kewangan,
                "SETIAUSAHA":invoice.SETIAUSAHA,
                "BENDAHARI":invoice.BENDAHARI,
                "JAWATANKUASA_PERALATAN_DAN_TEKNIKAL":invoice.JAWATANKUASA_PERALATAN_DAN_TEKNIKAL,
                "JAWATANKUASA_JEMPUTAN":invoice.JAWATANKUASA_JEMPUTAN,
                "JAWATANKUASA_AKTIVITI":invoice.JAWATANKUASA_AKTIVITI,
                "Tarikh_B":invoice.Tarikh_B,
                "Masa_B":invoice.Masa_B,
                "Tempat_B":invoice.Tempat_B,
                "JUMLAH_KESELURUHAN_1":invoice.JUMLAH_KESELURUHAN_1,
                "JUMLAH_KESELURUHAN_2":invoice.JUMLAH_KESELURUHAN_2,
                "Name_1":invoice.Name_1,


                "lineitem": lineitem,
                "lampiranc":lampiranc,
                "lampiranc2":lampiranc2,
                "lampirand":lampirand,
                "pengarah":pengarah,
                "timbalan":timbalan,
            }
    "return render(request, 'pdf1.html', context)"
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def update_data(request, id):
   
    invoice = get_object_or_404(Invoice, id=id)
    form = InvoiceForm(request.POST or None, instance=invoice)
    formset1 = LineItemForm(request.POST or None, instance=invoice)

    if form.is_valid() :
        form.save()
    
    if formset1.is_valid():
        formset1.save()
            
        for form in formset1:
            Masa_B1 = form.cleaned_data.get('Masa_B1')
            activity_B1 = form.cleaned_data.get('activity_B1')
            
            
            if Masa_B1 and activity_B1 :
                    
                
                LineItem(customer=invoice,
                            Masa_B1=Masa_B1,
                            activity_B1=activity_B1,
                            ).save()

        

        
    return render(request,'pdf_form/entry.html',{"form": form,'formset1':formset1})
    
def sign(request, id):
   
    qs = get_object_or_404(Invoice, id=id)
    form = InvoiceForm(request.POST or None, instance=qs)

    if request.method == 'GET':
        formset = signatureform_1(request.GET or None)
        form = InvoiceForm(request.GET or None)
    elif request.method == 'POST':
        formset = signatureform_1(request.POST)
    
    if form.is_valid() :
         invoice = Invoice.objects.get(instance=qs)
        
    if formset.is_valid():
            
        for form in formset:
            sign_1 = form.cleaned_data.get('sign_1')
            
            if sign_1 :
                    
                Signature_1(
                        model3=invoice,
                        sign_1=sign_1,
                        ).save()
        invoice.save()
        return redirect("/list")        
    context = {
        "formset": formset,
        
    }
    return render(request, 'pdf_form/verify_1.html', context)    
