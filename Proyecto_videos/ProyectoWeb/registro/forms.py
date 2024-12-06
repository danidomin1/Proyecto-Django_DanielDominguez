from django import forms
from django.contrib.auth.models import User

class RegistroForm(forms.ModelForm):
    class Meta:
        model = User  # Si estás usando el modelo User de Django
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
