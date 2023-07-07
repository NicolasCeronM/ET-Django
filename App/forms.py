from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
        widgets = {
            'first_name':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre'
                }
            ),

            'last_name':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su apellido'
                }
            ),

            'email':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'ejemplo@ejemplo.com'

                }
            ),

            'username':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su usuario'
                }
            ),
        }
        
