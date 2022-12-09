from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from . models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'brand', 'stock']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a name'}),
            'price':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter a price'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter a description'}),
            'brand':forms.Select(attrs={'class':'form-control'}),
            'category': forms.CheckboxSelectMultiple()
        } 
    
    # def __init__(self, *args, **kwargs):
    #     super(ProductForm, self).__init__(*args, **kwargs)   

        # for name, field in self.fields.items():
        #     if name != 'category':
        #         field.widget.attrs.update({'class': 'form-control', 'placeholder': f'Enter a {name}'})       