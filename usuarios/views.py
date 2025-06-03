from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        import pdb;
        #pdb.set_trace()
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'usuarios/home.html')
        else:
            return render(request, 'usuarios/login.html', {'form': form, 'error': 'Erro: usuário ou senha inválidos.'})
    else:
        form = AuthenticationForm()
        return render(request, 'usuarios/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'usuarios/home.html')
        else:
            return render(request, 'usuarios/register.html', {'form': form, 'error': 'Erro: por favor corrija os erros abaixo.'})
    else:
        form = CustomUserCreationForm()
        return render(request, 'usuarios/register.html', {'form': form})

def password_reset_view(request):
    return render(request, 'usuarios/password_reset.html')

def home_view(request):
    return render(request, 'usuarios/home.html')

