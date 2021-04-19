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
    messages.info(request,"User data saved successfully.")
    if data['type'] == 'seller':
        return redirect('enlist')


@login_required(login_url='account_login')
def profile(request):
    user = request.user
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email
    userDetail = UserDetail.objects.get(user=user)
    contact = userDetail.contact
    location = userDetail.location
    context={'first_name':first_name, 'last_name':last_name, 'email':email, 'contact':contact, 'location':location}
    print(context)
    return render(request, 'store/profile.html', context)




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
    price = data['price']
    seller = request.user
    sellerDetail = UserDetail.objects.get(user=seller)

    if name_book == "" or name_author == "" or year_pub == "" or price == "":
        messages.error(request,"All the fields are compulsory.")
        context={'sellerDetail': sellerDetail}
        return render(request, 'store/enlist.html',context, status=406)
    else:
        book = Book.objects.create(seller=request.user, name=name_book, author=name_author, year_of_publishing=year_pub, price=int(price))
        book.save()
        messages.info(request,"Product Enlisted Successfully!")
        context={'sellerDetail': sellerDetail}
        return render(request, 'store/enlist.html',context,status=201)



@login_required(login_url='account_login')
def enlistInstruments(request):
    data = request.POST
    name_instrument = data['name_instrument']
    price = data['price']
    seller = request.user
    sellerDetail = UserDetail.objects.get(user=seller)

    if name_instrument == "" or price == "":
        messages.error(request,"All the fields are compulsory.")
        context={'sellerDetail': sellerDetail}
        return render(request, 'store/enlist.html',context,status=406)
    else:
        sellerDetail = UserDetail.objects.get(user=seller)
        print(f"User is near {sellerDetail.location}")
        instrument = Instrument.objects.create(seller=request.user, name=name_instrument, price=int(price))
        instrument.save()
        messages.info(request,"Product Enlisted Successfully!")
        context={'sellerDetail': sellerDetail}
        return render(request, 'store/enlist.html',context,status=201)


@login_required(login_url='account_login')
def enlistLabcoats(request):
    data = request.POST
    size_labcoat = data['size_labcoat']
    price = data['price']
    seller = request.user
    sellerDetail = UserDetail.objects.get(user=seller)

    if size_labcoat == "" or price == "":
        messages.error(request,"All the fields are compulsory.")
        context={'sellerDetail': sellerDetail}
        return render(request, 'store/enlist.html',context, status=406)
    else:
        labcoat = Labcoat.objects.create(seller=request.user, size=size_labcoat, price=int(price))
        labcoat.save()
        messages.info(request,"Product Enlisted Successfully!")
        context={'sellerDetail': sellerDetail}
        return render(request, 'store/enlist.html',context, status=201)

