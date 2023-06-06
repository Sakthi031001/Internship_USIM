from django import forms
from django.forms import formset_factory
from .models import *
from datetime import *
from ckeditor.widgets import CKEditorWidget

class InvoiceForm(forms.ModelForm):
    class Meta:

        TARIKH = forms.DateField(label='TARIKH',widget=forms.DateInput(attrs={'type':'date','max':datetime.now().date()}))
        MASA = forms.TimeField(label='MASA',widget=forms.TimeInput(attrs={'type':'time'}))
        Tarikh_A = forms.DateField(label='TARIKH',widget=forms.DateInput(attrs={'type':'date','max':datetime.now().date()}))
        Tarikh_B = forms.DateField(label='TARIKH',widget=forms.DateInput(attrs={'type':'date','max':datetime.now().date()}))
        Masa_B = forms.TimeField(label='MASA',widget=forms.TimeInput(attrs={'type':'time'}))

        model = Invoice
        
        fields = ['TITLE','TEMPAT','ANJURAN','TUJUAN','LATAR_BELAKANG','Objektif_1','Tempat_A','Sasaran_peserta',
                  'Jawatankuasa_Pelaksana','Atur_Cara','Implikasi_Kewangan','SETIAUSAHA','BENDAHARI',
                  'JAWATANKUASA_PERALATAN_DAN_TEKNIKAL','JAWATANKUASA_JEMPUTAN','JAWATANKUASA_AKTIVITI',
                  'Atur_Cara_B','Tempat_B','Name_1','TARIKH','MASA','Tarikh_A','Tarikh_B','Masa_B',]

        labels = {'LATAR_BELAKANG':'LATAR BELAKANG','Objektif_1':'OBJEKTIF','Tempat_A':'Tempat',
                  'Sasaran_peserta':'SASARAN PESERTA','Jawatankuasa_Pelaksana':'JAWATANKUASA PELAKSANA',
                  'Atur_Cara':'ATUR CARA','Implikasi_Kewangan': 'IMPLIKASI KEWANGAN',
                  'JAWATANKUASA_PERALATAN_DAN_TEKNIKAL':'JAWATANKUASA PERALATAN DAN TEKNIKAL',
                  'JAWATANKUASA_JEMPUTAN':'JAWATANKUASA JEMPUTAN','JAWATANKUASA_AKTIVITI':'JAWATANKUASA AKTIVITI',
                  'Atur_Cara_B':'TAJUK','Tempat_B':'TEMPAT','Name_1':'NAME','Tarikh_A':'TARIKH',
                  'Tarikh_B':'TARIKH','Masa_B':'MASA',}

    

class LineItemForm(forms.ModelForm):

    class Meta:
        model = LineItem
        
        fields = ['Masa_B1','activity_B1']
        
        labels = {'Masa_B1':'MASA','activity_B1':'ACTIVITY'}
        
        widgets = {'Masa_B1':forms.TimeInput(attrs={'type':'time','class': 'form-control',}),
                   'activity_B1':forms.TextInput(attrs={'class': 'form-control',})}
    
    
    # amount = forms.DecimalField(
    #     disabled = True,
    #     label='Amount $',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control input',
    #     })
    # )
    
LineItemFormset = formset_factory(LineItemForm, extra=1)

class LampiranCForm(forms.Form):

    value_1 = forms.CharField(
        label='VALUE',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            
            
        })
    )
    
    Amount_1 = forms.DecimalField(
        label='RM',
        widget=forms.TextInput(attrs={
            'class': 'form-control input rate',
            
        })
    )

LampiranCFormset = formset_factory(LampiranCForm, extra=1)

class LampiranC2Form(forms.Form):
    value_C1 = forms.CharField(
        label='PERBELANJAAN',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            
            
        })
    )
    
    Amount_C1 = forms.DecimalField(
        label='RM',
        widget=forms.TextInput(attrs={
            'class': 'form-control input rate',
            
        })
    )

LampiranC2Formset = formset_factory(LampiranC2Form, extra=1)

class LampiranDForm(forms.Form):

    field = forms.CharField(
        label='FIELD',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            
            
        })
    )
    
    data = forms.CharField(
        label='DATA',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            
            
        })
    )

LampiranDFormset = formset_factory(LampiranDForm, extra=1)

class pengarahForm(forms.Form):
    
    PENGARAH = forms.CharField(
        label='PENGARAH',
         widget=forms.TextInput(attrs={
            'class': 'form-control',    
            
        })
    )
pengarahFormset = formset_factory(pengarahForm, extra=1)


class timbalanForm(forms.Form):
    
    TIMBALAN_PENGARAH = forms.CharField(
    label='TIMBALAN PENGARAH',
     widget=forms.TextInput(attrs={
            'class': 'form-control',    
        
    })
    )
timbalanFormset = formset_factory(timbalanForm, extra=1)


class UpdateInvoiceForm(forms.Form):

    class Meta:
        model = Invoice
        fields = ['TITLE','TEMPAT','ANJURAN','TUJUAN','LATAR_BELAKANG','Objektif_1','Tempat_A','Sasaran_peserta',
                  'Jawatankuasa_Pelaksana','Atur_Cara','Implikasi_Kewangan','SETIAUSAHA','BENDAHARI',
                  'JAWATANKUASA_PERALATAN_DAN_TEKNIKAL','JAWATANKUASA_JEMPUTAN','JAWATANKUASA_AKTIVITI',
                  'Atur_Cara_B','Tempat_B','Name_1','TARIKH','MASA','Tarikh_A','Tarikh_B','Masa_B',]
        
class signatureform_1(forms.Form):

    class Meta:
        model = Signature_1
        sign_1 = forms.ImageField()

signatureformset_1 = formset_factory(signatureform_1, extra=1)