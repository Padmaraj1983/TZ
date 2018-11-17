from django import forms
from registerForm.models import Register
class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields='__all__'