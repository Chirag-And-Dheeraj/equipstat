from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUsDetail
        fields = '__all__'
    firstName = forms.CharField(label="First Name " ,widget=forms.TextInput(attrs={'class': 'w-full bg-gray-500 text-gray-900 p-3 rounded placeholder-gray-700 focus:outline-none focus:shadow-myOutline', 'placeholder':'John'}))
    lastName = forms.CharField(label="Last Name ", widget=forms.TextInput(attrs={'class': 'w-full bg-gray-500 text-gray-900 p-3 rounded placeholder-gray-700 focus:outline-none focus:shadow-myOutline','placeholder':'Doe'}))
    email = forms.EmailField(label="Email " ,widget=forms.TextInput(attrs={'class': 'w-full bg-gray-500 text-gray-900 p-3 rounded placeholder-gray-700 focus:outline-none focus:shadow-myOutline','placeholder':'example@domain.com'}))
    contact = forms.CharField(label="Contact Number ",widget=forms.TextInput(attrs={'class': 'w-full bg-gray-500 text-gray-900 p-3 rounded placeholder-gray-700 focus:outline-none focus:shadow-myOutline','placeholder':'xxxxxxxxxx'}))
    typeOfMessage = forms.CharField(label="Type Of Message" ,widget=forms.RadioSelect(choices=MESSAGE_TYPES))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'w-full bg-gray-500 text-gray-900 p-3 rounded placeholder-gray-700 focus:outline-none focus:shadow-myOutline' ,'placeholder':'Type Your Messasge here...', 'rows':'4' , 'cols':'20'}),label="Enquiry/Grievances")


