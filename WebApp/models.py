from django.db import models

# Create your models here.
class RegistrationDB(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)
    C_Password = models.CharField(max_length=50,null=True,blank=True)
    E_Mail = models.CharField(max_length=50,null=True,blank=True)


class CartDB(models.Model):
    UserName = models.CharField(max_length=50, null=True, blank=True)
    ProductName = models.CharField(max_length=50, null=True, blank=True)
    Quantity = models.IntegerField( null=True, blank=True)
    Price = models.IntegerField( null=True, blank=True)
    TotalPrice = models.IntegerField( null=True, blank=True)
    Product_Image = models.ImageField(upload_to='Cart_Image', null=True, blank=True)

class OrderDB(models.Model):
    First_Name = models.CharField(max_length=50, null=True, blank=True)
    Last_Name = models.CharField(max_length=50, null=True, blank=True)
    Place = models.CharField(max_length=50, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Address = models.CharField(max_length=50, null=True, blank=True)
    State = models.CharField(max_length=50, null=True, blank=True)
    TotalPrice = models.IntegerField( null=True, blank=True)
    PIN_CODE = models.IntegerField( null=True, blank=True)
    Mobile_Number = models.IntegerField( null=True, blank=True)




class ContactDB(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    E_Mail = models.CharField(max_length=50,null=True,blank=True)
    Subject = models.CharField(max_length=50,null=True,blank=True)
    Message = models.CharField(max_length=500,null=True,blank=True)
