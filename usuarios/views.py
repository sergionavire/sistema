from django.shortcuts import render
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomUserLoginForm, CustomPasswordResetForm
from .models import Usuario


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request, data=request.POST)
        import pdb;
        #pdb.set_trace()
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'usuarios/home.html')
        else:
            return render(request, 'usuarios/login.html', {'form': form, 'error': 'Erro: usuário ou senha inválidos.'})
    else:
        form = CustomUserLoginForm()
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
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user = Usuario.objects.filter(email=form.cleaned_data['email']).first()
            if user:
                form.send_mail()
                return render(request, 'usuarios/password_reset.html', {'form': form, 'success': 'Instruções de redefinição de senha enviadas para o seu email.'})

        return render(request, 'usuarios/password_reset.html', {'form': form, 'error': 'Erro: por favor corrija os erros abaixo.'})
    else:
        form = PasswordResetForm()
        return render(request, 'usuarios/password_reset.html', {'form': form})

def home_view(request):
    return render(request, 'usuarios/home.html')

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url='/login/'