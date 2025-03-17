from django import forms
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)



class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = fields = ['username','email','password','first_name','last_name']