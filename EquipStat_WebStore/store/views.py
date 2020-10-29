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

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Invalid username or password')
                return redirect('login')
        else:
            return render(request, 'store/login.html')
    


def register(request):
    if request.method == 'POST':  # When the user fills the form, and submits it, the data comes as a POST request, because we have set the method as "POST" for security purpose.
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password_1 = request.POST['password1']
        password_2 = request.POST['password2']
        email = request.POST['email']
        contact = request.POST['contact']

        if password_1 == password_2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username not available!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password_2)
                user.save()
                userDetail = UserDetail.objects.create(user=user, contact=contact)
                messages.info(request, 'Yay, you just registered your account with us!')
                return redirect('login')
        else:
            messages.info(request, "Passwords don't match!")
            return redirect('register')
    else:  # This is a GET request, for fetching the registration page.
        return render(request, 'store/register.html')


# def password_reset(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             messages.success(request, 'Password reset successful!')
#             return redirect('password_reset')
#         else:
#             messages.error(request, 'Please correct the error below')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'accounts/password_reset.html', {'form': form})

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')



@login_required(login_url='login')
def profile(request, pk):
    user = User.objects.get(pk=pk)
    first_name = user.first_name
    last_name = user.last_name
    username = user.username
    email = user.email
    userDetail = UserDetail.objects.get(user_id=pk)
    contact = userDetail.contact

    listings = ProductRefurbished.objects.filter(seller=request.user)

    context = {
        'first_name': first_name,
        'last_name': last_name,
        'username': username,
        'email': email,
        'contact': contact,
        'listings': listings,
        }
    return render(request, 'store/profile.html', context)




def store(request):
    newProducts = ProductNew.objects.all()
    context = {'newProducts':newProducts}
    return render(request, 'store/store.html', context)


def refurbished(request):
    books = ProductRefurbished.objects.filter(typeOfProduct = 1)
    labCoats = ProductRefurbished.objects.filter(typeOfProduct = 2)
    instruments = ProductRefurbished.objects.filter(typeOfProduct = 3)

    context = { 'books' : books, 'labCoats' : labCoats, 'instruments' : instruments }
    return render(request, 'store/refurbished.html', context)


def product(request, slug):
    oneProduct = ProductNew.objects.get(slug=slug)
    context = {'oneProduct':oneProduct}
    return render(request, 'store/product.html', context )


def refurbishedProduct(request, slug):
    oneProduct = ProductRefurbished.objects.get(slug=slug)
    context = {'oneProduct':oneProduct}
    return render(request, 'store/refurbishedProduct.html', context )






@login_required(login_url='login')
def enlist(request):
    form = RefurbishedItemForm()
    if request.method == 'POST':
        form = RefurbishedItemForm(request.POST, request.FILES)
        if form.is_valid():
            formInstance = form.save(commit=False)
            formInstance.seller = request.user
            # formInstance.sellerID = request.user.id
            formInstance.save()
            return redirect('/')
        else:
            return HttpResponse('error while uploading')
    context = {'form':form}
    return render(request, 'store/enlist.html', context)


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


@login_required(login_url='login')
def cart(request):
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderlineitem_set.all()
    print(type(items))
    context = {'items': items, 'order':order}
    return render(request, 'store/cart.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action: ' ,action)
    print('ProductID: ',productId)

    customer = request.user
    product = ProductNew.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderLineItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
        
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was Added', safe=False)


def checkout(request):
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderlineitem_set.all()
    print(type(items))
    context = {'items': items, 'order':order}
    return render(request, 'store/checkout.html', context)