from django.shortcuts import render
from portfolios.models import Portfolio


def portfolio_index(request):
    portfolios = Portfolio.objects.all()
    context = {'portfolios': portfolios}
    return render(request, 'portfolio_index.html', context)


def portfolio_detail(request, pk):
    portfolio = Portfolio.objects.get(pk=pk)
    context = {'portfolio': portfolio}
    return render(request, 'portfolio_detail.html', context)