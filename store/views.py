from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json



# cartItems = Order.get_cart_items()


# Create your views here.
def home(request):
    context = {}
    return render(request, 'store/home.html', context)

def instruments(request):
    context={}
    return render(request, 'store/instruments.html', context)


def calculators(request):
    context={}
    return render(request, 'store/calculators.html', context)


def refurbishedBooks(request):
    context={}
    return render(request, 'store/refurbished-books.html', context)


def refurbishedLabcoats(request):
    context={}
    return render(request, 'store/refurbished-labcoats.html', context)


def refurbishedInstruments(request):
    context={}
    return render(request, 'store/refurbished-instruments.html', context)