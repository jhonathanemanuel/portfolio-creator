from urllib import request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify

from .forms import PortfolioForm, SectionFormSet
from portfolio.models import Portfolio
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login


def index(request):
    return render(request,'portfolio/index.html')

@login_required
def dashboard(request):
    portfolios = Portfolio.objects.filter(usuario=request.user).order_by('-date_added')

    context = {'portfolios': portfolios}

    return render(request, 'portfolio/dashboard.html', context)

@login_required
def editar_titulo_dashboard(request, pk):
    if request.method == 'POST':
        portfolio = get_object_or_404(Portfolio, pk=pk, usuario=request.user)
        novo_titulo = request.POST.get('titulo_titulo')
        if novo_titulo:
            portfolio.titulo_projeto = novo_titulo
            portfolio.save()

    return redirect('dashboard')

@login_required
def novo_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)

        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.usuario = request.user
            portfolio.slug = slugify(portfolio.titulo_projeto)
            if not portfolio.cor_fundo:
                portfolio.cor_fundo = "#f8f9fa"
            portfolio.save()
            return redirect('dashboard')
        else:
            print("ERROS DO FORMULÁRIO:", form.errors)
    else:
        form = PortfolioForm()

    context = {'form':form}
    return render(request,'portfolio/novo_portfolio.html', context)

def cadastrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    context = {'form':form}
    return render(request,'registration/cadastrar.html',context)

def detalhe_portifolio(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)
    context = {'portfolio':portfolio}
    return render(request, 'portfolio/visualizar.html', context)

@login_required
def editar_portfolio(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk, usuario=request.user)

    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        formset = SectionFormSet(request.POST, instance=portfolio)

        form_valido = form.is_valid()
        formset_valido = formset.is_valid()

        if form.is_valid():
            form.save()
            formset.save()
            print("SALVO")
            return redirect('editar_portfolio', pk=portfolio.pk)
        else:
            print("NÃO SALVO")
            print("ERRO NO FORM:", form.errors)
            print("ERRO NO FORMSET:", formset.errors)
    else:
        form = PortfolioForm(instance=portfolio)
        formset = SectionFormSet(instance=portfolio)

    context = {'form':form, 'portfolio':portfolio, 'formset':formset, 'edit_mode':True}

    return render(request, 'portfolio/visualizar.html', context)