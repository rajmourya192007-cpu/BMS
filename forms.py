from django import forms  
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
         model= Product
         fields='__all__'
         labels={
              'product_id':'Product ID',
              'name':'Name',
         }
         widgets={
              'product_id':forms.NumberInput(attrs={'placeholder':'e.g 1', 'class':'form-control'}),
              'Bookname':forms.TextInput(attrs={'placeholder':'e.g my book', 'class':'form-control'}),
         }
