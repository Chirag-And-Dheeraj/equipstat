from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def home(request):
    context = {}
    return render(request, 'store/home.html', context)

def store(request):
    newProducts = ProductNew.objects.all()
    context = {'newProducts':newProducts}
    return render(request, 'store/store.html', context)

def about(request):
    context = {}
    return render(request, 'store/about_us.html', context)

def contact(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'store/contact.html', context)

    context = {}
    return render(request, 'store/contact.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def product(request):
    context = {}
    return render(request, 'store/product.html', context)


