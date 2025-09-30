from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    Category_Name = models.CharField(max_length=50,blank=True,null=True)
    Category_Image = models.ImageField(upload_to="Category Images", blank=True, null=True)
    Category_Description = models.CharField(max_length=50, blank=True, null=True)


class ProductDB(models.Model):
    Category_Name = models.CharField(max_length=50, blank=True, null=True)
    Product_Name = models.CharField(max_length=50, blank=True, null=True)
    Product_Description = models.CharField(max_length=50, blank=True, null=True)
    Price = models.IntegerField(blank=True, null=True)
    Product_Image = models.ImageField(upload_to="Product Images", blank=True, null=True)
