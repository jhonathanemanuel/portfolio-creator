from urllib import request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .forms import PortfolioForm
from portfolio.models import Portfolio
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login


def index(request):
    return render(request,'portfolio/index.html')

@login_required
def dashboard(request):
    meus_portfolios = Portfolio.objects.all()
    # meus_portfolios = Portfolio.objects.filter(usuario=request.user)

    context = {'portfolios':meus_portfolios}

    return render(request,'portfolio/dashboard.html',context)

@login_required
def novo_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.usuario = request.user
            portfolio.save()
            return redirect('dashboard')
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
def editar_portifolio(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk, usuario=request.user)

    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            form = PortfolioForm(instance=portfolio)

        context = {'form':form, 'portfolio':portfolio}

        return render(request, 'portfolio/editar_portifolio.html', context)