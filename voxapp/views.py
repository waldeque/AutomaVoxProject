from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from .forms import CadastroForm, CadastroConta, CadastroCondominio, CadastroGrupoConta, CadastroInquilino
from django.contrib.auth import logout
from django.shortcuts import redirect

from .models import Condominio, Conta, GrupoConta, Inquilino


# Método para a página index
def index(request):
    return render(request, 'index.html', {})  # Abre o template index.html


def erro(request):
    return render(request, 'pagina_erro.html', {})  # Abre o template index.html


# @login_required
# Método para a Home page
def home(request):
    return render(request, 'home.html', {})  # Abre o template home.html


@login_required
# Método para a Home page
def homeu(request):
    return render(request, 'homeUser.html', {})  # Abre o template home.html


# Método para o Cadastro de Uuário
def cadastrar(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)  # Instancia do Formulário de Cadastro de Usuário na variável form.

        if form.is_valid():  # Verifica a validade do formulário instanciado anteriormente
            form.save()  # Salva os dados do Cadastro
            return HttpResponseRedirect("/login/")  # Redireciona para o login caso o cadastro seja bem sucedido
        else:
            return render(request, "cadastrar.html",
                          {"form": form})  # Retorna para o cadstro de usuário, pois deu erro

    return render(request, "cadastrar.html", {"form": CadastroForm()})


# Método para o cadastro de uma Conta
@login_required(login_url='/login/')
def cadastrar_conta(request):
    if request.method == 'POST':
        form = CadastroConta(request.POST)  # Instancia do Formulário de Cadastro de Contas na variavel form.

        if form.is_valid():  # Verifica a validade do formulário
            form.save()  # Salva os dados do Cadastro
            return HttpResponseRedirect(
                "/home/")  # Redireciona para a página inicial do Sistema, pois o cadastro do evento foi bem sucedido
        else:
            return render(request, "cadastrar_conta.html",
                          {"form": form})  # Volta para o cadastro de Conta, pois deu erro

    return render(request, "cadastrar_conta.html", {"form": CadastroConta()})


# Método para o cadastro de um Grupo de Contas
@login_required(login_url='/login/')
def cadastrar_grupo(request):
    if request.method == 'POST':
        form = CadastroGrupoConta(
            request.POST)  # Instancia do Formulário de Cadastro de Grupo de Contas na variavel form.

        if form.is_valid():  # Verifica a validade do formulário
            form.save()  # Salva os dados do Cadastro
            return HttpResponseRedirect(
                "/home/")  # Redireciona para a página inicial do Sistema, pois o cadastro do grupo foi bem sucedido
        else:
            return render(request, "cadastrar_grupo.html",
                          {"form": form})  # Volta para o cadastro do Evento, pois deu erro

    return render(request, "cadastrar_grupo.html", {"form": CadastroGrupoConta()})


# Método para o cadastro de um Condominio
@login_required(login_url='/login/')
def cadastrar_condominio(request):
    if request.method == 'POST':
        form = CadastroCondominio(request.POST)  # Instancia do Formulário de Cadastro de Condominio na variavel form.

        if form.is_valid():  # Verifica a validade do formulário
            form.save()  # Salva os dados do Cadastro
            return HttpResponseRedirect(
                "/home/")  # Redireciona para a página inicial do Sistema, pois o cadastro do Condominio foi bem sucedido
        else:
            return render(request, "cadastrar_condominio.html",
                          {"form": form})  # Volta para o cadastro do Condominio, pois deu erro

    return render(request, "cadastrar_condominio.html", {"form": CadastroCondominio()})


# Método para o cadastro de um Inquilino
@login_required(login_url='/login/')
def cadastrar_inquilino(request):
    if request.method == 'POST':
        form = CadastroInquilino(request.POST)  # Instancia do Formulário de Cadastro de Inquilino na variavel form.

        if form.is_valid():  # Verifica a validade do formulário
            form.save()  # Salva os dados do Cadastro
            return HttpResponseRedirect(
                "/home/")  # Redireciona para a página inicial do Sistema, pois o cadastro do Inquilino foi bem sucedido
        else:
            return render(request, "cadastrar_inquilino.html",
                          {"form": form})  # Volta para o cadastro do Inquilino, pois deu erro

    return render(request, "cadastrar_inquilino.html", {"form": CadastroInquilino()})


# Método para o login de usuário no Sistema
@csrf_exempt
def logar(request):
    if request.method == 'POST':
        form = AuthenticationForm(
            data=request.POST)  # Instancia do Formulário de Autenticaçao de Usuário na variável form.
        # form.fields['username'].widget.attrs['class'] = "form-signin"
        # form.fields['password'].widget.attrs['class'] = "form-signin"

        if form.is_valid():  # Verifica a validade do Formulário
            login(request, form.get_user())  # Realiza o login no Sistema
            # return HttpResponseRedirect("/")
            return render(request, 'homeUser.html',
                          {})  # Retorna para a página inicial do usuário pois o login foi bem sucedido
        else:
            return render(request, "login.html",
                          {"form": form})  # Volta para a página de login pois ocorreu erro do mesmo

    return render(request, 'login.html', {"form": AuthenticationForm()})


# return render_to_response("home_page.html", context_instance=RequestContext(request))
def logout_view(request):
    logout(request)
    return render(request, 'login.html', {})


# Método para a página de Inscrição em Eventos
@login_required(login_url='/login/')
def incricao_evento(request):
    return render(request, 'incricao_evento.html', {})  # Abre o template incricao_evento.html


def relatorio(request):
    """
    Função que realiza busca de evento de acordo com o qe foi digitado no campo de busca,
    """
    if request.method == 'GET':
        var_busca = request.GET.get('search_box')
        if var_busca is not None and var_busca is not "":
            contas = Conta.objects.filter(nome__icontains=var_busca).order_by('nome')
        else:
            contas = Conta.objects.all().order_by('nome')

        return render(request, 'relatorio.html', {'contas': contas})

    return home()
