from django import forms
from django.forms import ModelForm
from . models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phoneNo', 'address']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a name', 'autocomplete': 'off'}),
            'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter a email', 'autocomplete': 'off'}),
            'phoneNo':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a phoneNo', 'autocomplete': 'off'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter a address', 'autocomplete': 'off'}),
        } 