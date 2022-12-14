from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})


        # fields = ['first_name', 'last_name', 'username', 'email', 'password1']
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter a first name', 'autocomplete': 'off'}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter a last name', 'autocomplete': 'off'}),
        #     'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter a username', 'autocomplete': 'off'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Enter a email', 'autocomplete': 'off'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Enter a email', 'autocomplete': 'off'})
        # }
        # def __init__(self, *args, **kwargs):
        #     super(CustomUserCreationForm, self).__init__(*args, **kwargs)   

        #     for name, field in self.fields.items():
        #         field.widget.attrs.update({'class': 'form-control', 'placeholder': f'Enter a {name}'})   
