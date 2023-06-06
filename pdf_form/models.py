from django.db import models
import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class Invoice(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    TITLE = RichTextField(null=True)

    TARIKH = models.DateField(auto_now=False,auto_now_add=False,blank=True,null=True)
    MASA = models.TimeField(auto_now=False,auto_now_add=False,blank=True,null=True)
    TEMPAT = models.TextField(max_length=100, default='',blank=True,null=True)
    ANJURAN = models.TextField(max_length=300, default='',blank=True,null=True)

    TUJUAN = models.TextField(max_length=300, default='',blank=True,null=True)
    LATAR_BELAKANG = RichTextField(null=True)


    Objektif_1 = RichTextField(null=True)


    Butiran_program = models.TextField(max_length=0, default='',blank=True,null=True)
    Tarikh_A = models.DateField(auto_now=False,auto_now_add=False,blank=True,null=True)
    Tempat_A = models.TextField(max_length=50, default='',blank=True,null=True)
    Sasaran_peserta = models.TextField(max_length=50, default='',blank=True,null=True)
    Jawatankuasa_Pelaksana = models.TextField(max_length=50, default='',blank=True,null=True)
    Atur_Cara = models.TextField(max_length=50, default='',blank=True,null=True)
    Implikasi_Kewangan = models.TextField(max_length=50, default='',blank=True,null=True)


    SETIAUSAHA = models.TextField(max_length=50, default='',blank=True,null=True)
    BENDAHARI = models.TextField(max_length=50, default='',blank=True,null=True)
    JAWATANKUASA_PERALATAN_DAN_TEKNIKAL = models.TextField(max_length=50, default='',blank=True,null=True)
    JAWATANKUASA_JEMPUTAN = models.TextField(max_length=50, default='',blank=True,null=True)
    JAWATANKUASA_AKTIVITI = models.TextField(max_length=50, default='',blank=True,null=True)

    Atur_Cara_B = models.TextField(max_length=100, default='',blank=True,null=True)
    Tarikh_B = models.DateField(auto_now=False,auto_now_add=False,blank=True,null=True)
    Masa_B = models.TimeField(auto_now=False,auto_now_add=False,blank=True,null=True)
    Tempat_B = models.TextField(max_length=50, default='',blank=True,null=True)
   
    JUMLAH_KESELURUHAN_1 = models.IntegerField(blank=True,null=True)

    JUMLAH_KESELURUHAN_2 = models.IntegerField(blank=True,null=True)

    status = models.BooleanField(default=False)

    Name_1 = models.TextField(max_length=50, default='',blank=True,null=True)



    def __str__(self):
        return self.user.username

    # def save(self, *args, **kwargs):
        # if not self.id:             
        #     self.due_date = datetime.datetime.now()+ datetime.timedelta(days=15)
        # return super(Invoice, self).save(*args, **kwargs)

class LineItem(models.Model):
    customer = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    Masa_B1 = models.TimeField(auto_now=False,auto_now_add=False,blank=True,null=True)
    activity_B1 = models.TextField(max_length=100, default='',blank=True,null=True)
    

    """service = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.DecimalField(max_digits=9, decimal_places=2)"""

    def __str__(self):
        return str(self.customer)

class LampiranC(models.Model):
    modelC = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    Amount_1 = models.IntegerField(blank=True,null=True)
    value_1 = models.TextField(max_length=50, default='',blank=True,null=True)

    def __str__(self):
        return str(self.modelC)
    
class LampiranC2(models.Model):
    modelC2 = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    Amount_C1 = models.IntegerField(blank=True,null=True)
    value_C1 = models.TextField(max_length=50, default='',blank=True,null=True)

    def __str__(self):
        return str(self.modelC2)

class LampiranD(models.Model):
    modelD = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    field = models.TextField(max_length=50, default='',blank=True,null=True)
    data = models.TextField(max_length=50, default='',blank=True,null=True)

    def __str__(self):
        return str(self.modelD)
    
class Pengarah(models.Model):
    model1 = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    PENGARAH = models.TextField(max_length=50, default='',blank=True,null=True) 

    def __str__(self):
        return str(self.model1)

class Timbalan(models.Model):
    model2 = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    TIMBALAN_PENGARAH = models.TextField(max_length=50, default='',blank=True,null=True) 

    def __str__(self):
        return str(self.model2)

class Signature_1(models.Model):
    model3 = models.ForeignKey(Invoice, on_delete=models.CASCADE) 
    sign_1 = models.ImageField()

    def __str__(self):
        return str(self.model3)



