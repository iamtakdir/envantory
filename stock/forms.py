from django import forms
from django.db import models
from django.db.models import fields
from .models import Stock,Supplier,Category

class Add_stock_form (forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category','item_name', 'quantity','price','amount', 'supplier']

    

class Add_Sup_form (forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['sup_name','sup_mobile','sup_email','sup_note']

class Add_Category_form (forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name']