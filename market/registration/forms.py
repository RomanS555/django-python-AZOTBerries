
from django.forms import ModelForm
from django import forms
from . import models

class RegistrationForm(ModelForm):
    password1 = forms.CharField(        
        widget=forms.PasswordInput(attrs={'class': 'form-control',"id":"password_confirm"}),
        label="Подтвердите пароль",
        
        
        max_length=32,  
        required=True,   
        help_text="Введите пароль еще раз для подтверждения"  
        )
    class Meta:
        model = models.ShopUser
        fields = ['login','password']
        widgets = {
            'login': forms.TextInput(attrs={'class': 'form-control', "id":"login"}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', "id":"password"}),}
        
class LoginForm(ModelForm):
    
    class Meta:
        model = models.ShopUser
        fields = ['login','password']
        widgets = {
            'login': forms.TextInput(attrs={'class': 'form-control', "id":"login"}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', "id":"password"}),}
        
        
   
        

        
    
    