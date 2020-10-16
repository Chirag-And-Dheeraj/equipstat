from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
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


def logout(request):
    auth.logout(request)
    return redirect('/')



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


