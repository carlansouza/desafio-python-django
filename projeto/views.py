from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import TaskForm




@login_required
def home(request):
    return render(request, 'projeto/pages/home.html')


def relatorio(request):
    return render(request, 'projeto/pages/relatorios.html')

def cadastrar(request):
    return render(request, 'projeto/pages/cadastrar_vaga.html')

def cadastar_vaga(request):
    form = TaskForm()
    return render(request, 'projeto/pages/cadastrar_vaga.html', {'form': form})



def cadastrar_usuario(request):
    if request.method == 'POST':
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('home')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'registration/cadastrar_usuario.html', {'form_usuario': form_usuario})

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

