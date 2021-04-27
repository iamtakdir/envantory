from datetime import timezone
from django.db import models



# Create your models here.

class Category (models.Model):
    cat_name= models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.cat_name


class Supplier (models.Model):
    sup_name = models.CharField(max_length=200, null=True,)
    sup_mobile = models.CharField(max_length=200, null=True, blank=True)
    sup_email = models.CharField(max_length=200, null=True, blank=True)
    sup_note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.sup_name

class Stock( models.Model):
    category =models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,blank=True)
    item_name = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(blank=True, null=True, default=0)
    price = models.FloatField(null=True, blank=True,default= 0)
    amount = models.FloatField(null=True, blank=True,default= 0)
    supplier= models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True,blank=True)
    last_updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    timestamp= models.DateTimeField(auto_now_add=True,auto_now=False,)
    def __str__(self):
        itemname=str(self.item_name)
        return itemname








