from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from django import forms

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'juan@gmail.com'}))
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Ingrese Password'})
    )
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Reingrese Password', 'min': 8})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Usuario'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control validate', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

class UserEditForm(UserChangeForm):
    password = None  # Oculta el campo de contraseña en el formulario de edición de perfil
    username = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Usuario'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'juan@gmail.com'}))
    first_name = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Juan'}))
    last_name = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Perez'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        exclude = ['password']