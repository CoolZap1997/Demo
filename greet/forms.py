from .models import Person
from django import forms
from django.forms import ModelForm

class AuthorForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'gender', 'email', 'pincode', 'phone']
        