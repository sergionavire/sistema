from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from usuarios.models import Usuario

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username', 'password1', 'password2')
