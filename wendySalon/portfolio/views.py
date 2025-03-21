from django.shortcuts import render
from django.views import generic
from .models import Portfolio
# Create your views here.
def index(reuqest):
    portfolio_list = Portfolio.objects.all()
    context = {'portfolio_list': portfolio_list}
    return render(reuqest, 'portfolio/index.html', context)
# class IndexView(generic.ListView):
