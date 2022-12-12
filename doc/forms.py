from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'rows': 3,
                                                                            'cols': 20, 'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'rows': 3,
                                                                                 'cols': 20, 'placeholder': 'Пароль'}))
    class Meta:
        model = User

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'rows': 3,
                                                                            'cols': 20, 'placeholder': 'Логин'}))
    phone = forms.EmailField(label='Почта', widget=forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'myemail@gmail.com'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                                  'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                                         'placeholder': 'Повтор пароля'}))
