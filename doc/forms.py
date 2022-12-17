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
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                    label='Номер телефона',
                                    widget=forms.NumberInput(attrs={'class': 'form-input',
                                                                    'placeholder':'Номер телефона',
                                                                    'type': 'phone'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                                  'placeholder': 'Пароль',}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                                         'placeholder': 'Повтор пароля'}))
    class Meta:
        model = User
        fields = ('username', 'phone_number', 'password1', 'password2',)
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
