from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json



# Create your views here.
def home(request):
    context = {}
    return render(request, 'store/home.html', context)


def collectUserData(request):
    data = request.POST
    contact = data['contact_user']
    location = data['location_user']
    userDetail = UserDetail.objects.create(user=request.user, contact=contact, location=location)
    messages.info(request,"User data saved successfully. For God's sake, please complete atleast this feature today.")
    if data['type'] == 'seller':
        return redirect('enlist')

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


@login_required(login_url='account_login')
def enlist(request):
    try:
        sellerDetail = UserDetail.objects.get(user = request.user)
    except:
        sellerDetail = None
    context={'sellerDetail': sellerDetail}
    return render(request, 'store/enlist.html',context)


@login_required(login_url='account_login')
def enlistBooks(request):
    data = request.POST
    name_book = data['name_book']
    name_author = data['name_author']
    year_pub = data['year_pub']
    price = int(data['price'])

    if name_book == "" or name_author == "" or year_pub == "" or price == "":
        messages.error(request,"All the fields are compulsory.")
        return render (request, 'store/enlist.html', status=406)
    else:
        seller = request.user
        try:
            sellerDetail = UserDetail.objects.get(user=seller)
            print(f"User is near {sellerDetail.location}")
            book = Book.objects.create(seller=request.user, name=name_book, author=name_author, year_of_publishing=year_pub, price=price)
            book.save()
            messages.info(request,"Product Enlisted Successfully!")
            context={'sellerDetail': sellerDetail}
            return render(request, 'store/enlist.html',context)
        except:
            messages.error(request,"User has not provided his/her/their location. What the fuck do you plan on doing?")
            print("User has not provided his/her/their location. What the fuck do you plan on doing?")
            return render (request, 'store/enlist.html', status=406)
        