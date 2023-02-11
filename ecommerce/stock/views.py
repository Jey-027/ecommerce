from django.shortcuts import render
from .forms import ProductForm, PurchaseForm, PizzaForm

def index(request):
    return render(request, 'index.html', {})


def create_producto(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = ProductForm()
        return render(request, 'product.html', {"form": form})
    
    return render(request, 'index.html', {})
    

def purchase(request):
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PurchaseForm()
        return render(request, 'purchase.html', {"form": form})

    return render(request, 'index.html', {})


def pizza(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PizzaForm()
        return render(request, 'pizza.html', {"form": form})

    return render(request, 'index.html', {})