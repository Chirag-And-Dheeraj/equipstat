from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms




class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUsDetail
        fields = '__all__'
    firstName = forms.CharField(label="First Name " ,widget=forms.TextInput(attrs={'class':'w-full bg-gray-500 text-gray-900 placeholder-gray-700 p-3 rounded focus:outline-none focus:shadow-myOutline' , 'placeholder':'First Name'}))
    lastName = forms.CharField(label="Last Name ", widget=forms.TextInput(attrs={'class':'w-full bg-gray-500 text-gray-900 placeholder-gray-700 p-3 rounded focus:outline-none focus:shadow-myOutline ','placeholder':'Last Name'}))
    email = forms.EmailField(label="Email " ,widget=forms.TextInput(attrs={'class':'w-full bg-gray-500 text-gray-900 placeholder-gray-700 p-3 rounded focus:outline-none focus:shadow-myOutline ','placeholder':'Email Address'}))
    contact = forms.CharField(label="Contact Number ",widget=forms.TextInput(attrs={'class':'w-full bg-gray-500 text-gray-900 placeholder-gray-700 p-3 rounded focus:outline-none focus:shadow-myOutline ','placeholder':'Contact'}))
    typeOfMessage = forms.CharField(label="Type Of Message" ,widget=forms.RadioSelect(choices=MESSAGE_TYPES))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'w-full bg-gray-500 text-gray-900 placeholder-gray-700 p-3 rounded focus:outline-none focus:shadow-myOutline ' ,'placeholder':'Type Your Messasge here...', 'rows':'4' , 'cols':'20'}),label="Enquiry/Grievances")


