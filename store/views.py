from django.shortcuts import render, redirect
from .models import Product
from .forms import AddProductForm
# Create your views here.


def index(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request, 'store/index.html', context)


def products(request):
    return render(request, 'store/product.html')


def add_product(request):
    form = AddProductForm
    if request.method == "POST":
        new_product = AddProductForm(request.POST)
        if new_product.is_valid():
           new_product.save()
        return redirect('home')
    
    context = {"form":form}
    return render(request, 'store/add_product.html', context)