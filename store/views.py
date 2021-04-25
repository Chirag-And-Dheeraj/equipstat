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
    userDetail = UserDetail.objects.create(
        user=request.user, contact=contact, location=location)
    messages.success(request, "Profile details saved")
    if data['type'] == 'seller':
        return redirect('enlist')


@login_required(login_url='account_login')
def profile(request):
    user = request.user
    first_name = user.first_name
    last_name = user.last_name
    email = user.email
    try:
        userDetail = UserDetail.objects.get(user=user)
        contact = userDetail.contact
        location = userDetail.location
    except:
        contact = ""
        location = ""
    context = {'first_name': first_name, 'last_name': last_name,
               'email': email, 'contact': contact, 'location': location}

    try:
        listings_books = Book.objects.filter(seller=userDetail)
        print(listings_books)
    except:
        listings_books = None
        print("No Book Listing")

    try:
        listings_instruments = Instrument.objects.filter(seller=userDetail)
        print(listings_instruments)
    except:
        listings_instruments = None
        print("No Instrument Listing")

    try:
        listings_labcoats = Labcoat.objects.filter(seller=userDetail)
        print(listings_labcoats)
    except:
        listings_labcoats = None
        print("No Labcoat Listing")

    if request.method == "POST":
        data = request.POST
        new_contact = data['contact']
        new_location = data['location']
        try:
            userDetail = UserDetail.objects.get(user=request.user)
            userDetail.contact = new_contact
            userDetail.location = new_location
            userDetail.save()
            contact = userDetail.contact
            location = userDetail.location
            context = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'contact': contact,
                'location': location,
                'listings_books': listings_books,
                'listings_labcoats': listings_labcoats,
                'listings_instruments': listings_instruments
            }
            messages.info(request, "Profile details updated")
            return render(request, 'store/profile.html', context, status=200)
        except:
            userDetail = UserDetail.objects.create(
                user=request.user, contact=new_contact, location=new_location)
            userDetail.save()
            contact = userDetail.contact
            location = userDetail.location
            context = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'contact': contact,
                'location': location,
                'listings_books': listings_books,
                'listings_labcoats': listings_labcoats,
                'listings_instruments': listings_instruments
            }
            messages.success(request, "Profile details saved")
            return render(request, 'store/profile.html', context, status=201)
    else:
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'contact': contact,
            'location': location,
            'listings_books': listings_books, 'listings_labcoats': listings_labcoats, 'listings_instruments': listings_instruments
        }
        return render(request, 'store/profile.html', context)


def instruments(request):
    context = {}
    return render(request, 'store/instruments.html', context)


def calculators(request):
    context = {}
    return render(request, 'store/calculators.html', context)


def refurbishedBooks(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'store/refurbished-books.html', context)


def refurbishedInstruments(request):
    instruments = Instrument.objects.all()
    context = {'instruments': instruments}
    return render(request, 'store/refurbished-instruments.html', context)


def refurbishedLabcoats(request):
    context = {}
    return render(request, 'store/refurbished-labcoats.html', context)


@login_required(login_url='account_login')
def enlist(request):
    try:
        sellerDetail = UserDetail.objects.get(user=request.user)
    except:
        sellerDetail = None
    context = {'sellerDetail': sellerDetail}
    return render(request, 'store/enlist.html', context)


@login_required(login_url='account_login')
def enlistBooks(request):
    if request.method == 'POST':
        data = request.POST
        name_book = data['name_book']
        name_author = data['name_author']
        year_pub = data['year_pub']
        price = data['price']
        description = data['description']
        images = request.FILES.getlist('images[]')
        seller = request.user
        sellerDetail = UserDetail.objects.get(user=seller)
        if name_book == "" or name_author == "" or year_pub == "" or price == "" or description == "":
            messages.error(request, "All the fields are compulsory")
            return redirect('enlist')
        else:
            book = Book.objects.create(seller=sellerDetail, name=name_book, author=name_author, year_of_publishing=year_pub, price=int(price), description=description)
            book.save()
            newBook = Book.objects.get(id=book.id)
            print(images)
            for image in request.FILES.getlist('images[]'):
                print(image)
                bookImage = BookImage.objects.create(book=newBook, image=image)
                print(f"{bookImage.book.name} image is inside {bookImage.imageURL}")
                bookImage.save()
            messages.success(request, "Product enlisted successfully")
            return redirect('enlist')
    else:
        return redirect('enlist')



@login_required(login_url='account_login')
def enlistInstruments(request):
    if request.method == 'POST':
        data = request.POST
        name_instrument = data['name_instrument']
        price = data['price']
        description = data['description']
        seller = request.user
        sellerDetail = UserDetail.objects.get(user=seller)

        if name_instrument == "" or price == "" or description == "":
            messages.error(request, "All the fields are compulsory")
            return redirect('enlist')
        else:
            sellerDetail = UserDetail.objects.get(user=seller)
            print(f"User is near {sellerDetail.location}")
            instrument = Instrument.objects.create(
                seller=sellerDetail, name=name_instrument, price=int(price), description=description)
            instrument.save()
            newInstrument = Instrument.objects.get(id=instrument.id)
            for image in request.FILES.getlist('images[]'):
                instrumentImage = InstrumentImage.objects.create(instrument=newInstrument, image=image)
                print(f"{instrumentImage.instrument.name} image is inside {instrumentImage.imageURL}")
                instrumentImage.save()
            messages.success(request, "Product enlisted successfully")
            return redirect('enlist')
    else:
        return redirect('enlist')


@login_required(login_url='account_login')
def enlistLabcoats(request):
    if request.method == 'POST':
        data = request.POST
        size_labcoat = data['size_labcoat']
        price = data['price']
        description = data['description']
        seller = request.user
        sellerDetail = UserDetail.objects.get(user=seller)

        if size_labcoat == "" or price == "" or description == "":
            messages.error(request, "All the fields are compulsory")
            return redirect('enlist')
        else:
            labcoat = Labcoat.objects.create(
                seller=sellerDetail, size=size_labcoat, price=int(price), description=description)
            labcoat.save()
            newLabcoat = Labcoat.objects.get(id=labcoat.id)
            for image in request.FILES.getlist('images[]'):
                labcoatImage = LabcoatImage.objects.create(labcoat=newLabcoat, image=image)
                print(f"{labcoatImage.labcoat.size} image is inside {labcoatImage.imageURL}")
                labcoatImage.save()
            messages.success(request, "Product enlisted successfully")
            return redirect('enlist')
    else:
        return redirect('enlist')
