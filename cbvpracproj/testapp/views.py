from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from testapp.models import Cart
# Create your views here.

class CartListView(ListView):
    model=Cart

class CartDetailView(DetailView):
    model=Cart

class CartCreateView(CreateView):
    model=Cart
    fields=('itemname','qty','price')

class CartUpdateView(UpdateView):
    model=Cart
    fields=('itemname','qty','price')

