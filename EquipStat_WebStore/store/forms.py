from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUsDetail
        fields = '__all__'
    firstName = forms.CharField(label="First Name ")
    lastName = forms.CharField(label="Last Name ")
    email = forms.EmailField(label="Email ")
    contact = forms.CharField(label="Contact Number ")
    typeOfMessage = forms.CharField(widget=forms.Select(choices=MESSAGE_TYPES))
    message = forms.CharField(widget=forms.Textarea(),label="Enquiry/Grievances ")
