from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class ContactUsForm(ModelForm):
    firstName = forms.CharField(label="First Name " ,widget=forms.TextInput(attrs={'class': 'w-full bg-gray-500 text-gray-900 p-3 rounded placeholder-gray-700 focus:outline-none focus:shadow-myOutline', 'placeholder':'John'}))
    lastName = forms.CharField(label="Last Name ", widget=forms.TextInput(attrs={'class': 'w-full bg-gray-500 text-gray-900 p-3 rounded placeholder-gray-700 focus:outline-none focus:shadow-myOutline','placeholder':'Doe'}))
    email = forms.EmailField(label="Email " ,widget=forms.TextInput(attrs={'class': 'w-full bg-gray-500 text-gray-900 p-3 rounded placeholder-gray-700 focus:outline-none focus:shadow-myOutline','placeholder':'example@domain.com'}))
    contact = forms.CharField(label="Contact Number ",widget=forms.TextInput(attrs={'class': 'w-full bg-gray-500 text-gray-900 p-3 rounded placeholder-gray-700 focus:outline-none focus:shadow-myOutline','placeholder':'xxxxxxxxxx'}))
    typeOfMessage = forms.CharField(label="Type Of Message" ,widget=forms.RadioSelect(choices=MESSAGE_TYPES))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'w-full bg-gray-500 text-gray-900 p-3 rounded placeholder-gray-700 focus:outline-none focus:shadow-myOutline' ,'placeholder':'Type Your Messasge here...', 'rows':'4' , 'cols':'20'}),label="Feedback/Grievances")

    class Meta:
        model = ContactUsDetail
        fields = '__all__'

class RefurbishedItemForm(ModelForm):
    name = forms.CharField(label="Product Name " ,widget=forms.TextInput(attrs={'class': 'w-full bg-gray-500 text-gray-900 p-3 rounded placeholder-gray-700 focus:outline-none focus:shadow-myOutline', 'placeholder':'Book name, LabCoat, ...'}))
    typeOfProduct = forms.CharField(label="Type Of Product " ,widget=forms.RadioSelect(choices=TYPES))
    expectedReturn = forms.CharField(label="Expected Return ",widget=forms.TextInput(attrs={'class': 'w-full bg-gray-500 text-gray-900 p-3 rounded placeholder-gray-700 focus:outline-none focus:shadow-myOutline','placeholder':'xxx'}))
    image = forms.ImageField(label="Upload Image")
    details = forms.CharField(widget=forms.Textarea(attrs={'class': 'w-full bg-gray-500 text-gray-900 p-3 rounded placeholder-gray-700 focus:outline-none focus:shadow-myOutline' ,'placeholder':'Type Product Details here...', 'rows':'3' , 'cols':'20'}),label="Product Details ")
    class Meta:
        model = ProductRefurbished
        # fields = '__all__'
        exclude = ['slug' , 'seller']