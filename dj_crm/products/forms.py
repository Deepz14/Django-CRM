from django.forms import ModelForm
from django import forms
from . models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'brand', 'stock']
        widgets = {'category': forms.CheckboxSelectMultiple()}
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)     

        for name, field in self.fields.items():
            if name != 'category':
                field.widget.attrs.update({'class': 'form-control'})  